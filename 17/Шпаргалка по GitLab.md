### 1. Global keywords / Глобальные ключевые слова

```
# 1. [ default ]

# Если в джобе не определен соответствующий keyword, то он будет подгружен из default (как например в джобе default_run)
default:
  image: python:3.9

default_run:
  script: <>

latest_run:
  image: python:latest
  script: <>


# 2. [ stages ] 

# Джобы внутри одного стейджа запускаются параллельно. Джобы из последующего стейджа запускаются, только когда все джобы из предыдущего завершаются успешно. Если одна из джоб падает, то параллельные ей продолжают работу, но в целом пайплайн помечается как failed и последующие стейджи не запускаются.
stages:
  - style_checks
  - build_test_samples
  - update_cases_statuses

flake8-check:
  stage: style_checks


# 3. [ include ] 

# Позволяет подгрузить внешний конфиг
# include:local
# include:project
# include:remote
# include:template
include:
  - local: .gitlab/ci/skip.yml
    rules:
      - <>
  - local: .gitlab/ci/*.gitlab-ci.yml
    rules:
      - <>


# 4. [ variables ]


# 5. [ workflow ] 

# Позволяет регулировать поведение на уровне пайплайна. Например, с помощью правил пайплайн можно запустить или нет в зависимости от условия.
# workflow:rules: name
# workflow:rules: if
# workflow:rules: changes
# workflow:rules: exists
# workflow:when: always / never
# workflow:variables
workflow:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "push"'
    - if: '$CI_PIPELINE_SOURCE != "schedule"

```
### 2. Jobs keywords / Ключевые слова уровня джобы

```
# 1. [ after_script ] 

# Команды будут запускаться после каждой джобы (даже упавшей). 
# Важно: запускается в новой оболочке, то есть не имеет доступа к изменениям из предыдущих этапов (before_script или script). 
# Не влияет на код возврата основной джобы - даже если after_script упадет, то финальный результат все равно будет 0.	
job:
  script:
    - ls
  after_script:
    - rm -rf /tmp/test


# 2. [ allow_failure ] 

# Позволяет указать, будет ли дальше исполняться пайплайн, если джоба упала.	
test_job_1:
  script:
    - ls
    - exit 1
  allow_failure:
    exit_codes: 145


# 3. [ artifacts ] 

# По дефолту артефакты собираются только для успешных джоб.
# artifacts:paths
# artifacts:exclude
# artifacts:expire_in
# artifacts:expose_as
# artifacts:name
# artifacts:public
# artifacts:reports
# artifacts:untracked
# artifacts:when
job:
  artifacts:
    paths:
      - app.log
      - configs/
  exclude:
    - configs/**/*.bin expire_in: 3 weeks and 1 day
    name: "artifacts-file"
    

# 4. [ before_script ]	


# 5. [ cache ] 

# Шарим список файлов/директорий между разными джобами (могут использоваться пути только из рабочей директории). Кэш может использоваться последующими пайплайнами/джобами.
# cache:paths
# cache:key
# cache:key:files
# cache:key:prefix
# cache:untracked
# cache:unprotect
# cache:when
# cache:policy
# cache:fallback_keys
default:
  image: python:latest
  cache:                      
    paths:                    
      - .cache/pip
  before_script:
    - source venv/bin/activate

variables:  
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"

test:
  script:
    - pytest <…>


# 6. [ coverage ] 

# Ищем лог джобы на предмет совпадения с регулярным выражением для оценки покрытия.	my_job:
  script: <>
  coverage: ‘/Coverage: \d+/'


# 7. [ dast_configuration ] 

# Dynamic Application Security Testing (DAST) - проверка приложения на уязвимости.	
dast:
  dast_configuration:
    site_profile: "Site profile"
    scanner_profile: "Test"


# 8. [ dependencies ] 

# Позволяет указать список джобы, из которых нужно взять артефакты.	
job:
  stage: <>
  script: <>
  dependencies:
    - another_job


# 9. [ environment ] 

# Окружение описывает, куда будет деплоиться код (production, staging и т д)
# environment:name
# environment:url
# environment:on_stop
# environment:action start / prepare / stop / verify / access
# environment:auto_stop_in
# environment:kubernetes
# environment:deployment_tier
deploy to staging:
  stage: deploy
  script: git push staging HEAD:main
  environment: staging


# 10. [ extends ] 

# Позволяет переиспользовать часть текущего конфига. Аналог YAML anchors.	
.template_job:
  script: <>
  stage: <>
  only:
    refs:
      - branches

job:
  extends: .template_job
  script: <>
  only:
    variables:
      - $JOB_ID


# 11. [ image ] 

# Указывает Docker image
image:entrypoint
image:pull_policy always / if-not-present / never	image: python:3.9


# 12. [ inherit ] 

# Конфигурирует правила наследования дефолтных keywords и переменных
# inherit:default
# Inherit:variables
job:
  script: echo "It doesnt inherit global vars"
  inherit:
    variables: false


# 13. [ interruptible ] 

# Если установлен в true, то запущенная джобы должна быть остановлена, если запущен более новый пайплайн.	
job1:
  stage: stage1
  script:
    - echo “To cancel”
  interruptible: true

job2:
  stage: stage2
  script:
    - echo “No cancellation”


# 14. [ needs ]  

# Позволяет указать джобы, которые должны быть запущены вне очереди.
# needs:artifacts
# needs:project
# needs:pipeline:job
# needs:optional
# needs:pipeline
# needs:parallel:matrix	
job1:
  stage: <>
  needs: [“job2”]
  script: <>

job2:
  stage: <>
  script: <>


# 15. [ only / except ] 

# Используются, чтобы добавлять (only) или исключать (except) джобы из пайплайна
# only:variables / except:variables
# only:changes / except:changes
# only:kubernetes / except:kubernetes	
job:
  script: <>
  only:
    variables:
      - $ENV == "stg"
    changes:
      - samples/*


# 16. [ pages ] 

# Позволяет сконфигурировать Gitlab Pages - разворачивание статических веб сайтов прямо из репозитория
pages:publish
	pages:
  script:
    - mv my-html-page public_folder
  artifacts:
    paths:
      - public
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
  environment: production


# 17. [ parallel ] 

# Позволяет запустить одну джобу несколько раз в параллель
parallel:matrix
	job:
  script: pytest
  parallel: 6


# 18. [ release ] 

# Позволяет создать релиз (по тэгу)
# release:tag_name
# release:tag_message
# release:name
# release:description
# release:ref
# release:milestones
# release:released_at
# release:assets:links
job:
  stage: <>
  image: release-cli:latest
  rules:
    - if: $CI_COMMIT_TAG               
  script:
    - <>
  release:
    tag_name: $CI_COMMIT_TAG
    name: 'Release $CI_COMMIT_TAG'


# 19. [ resource_group ] 

# Реализует семафор - объект, позволяющий войти в заданный участок кода не более чем N потокам. 
# То есть в случае с resource_group только одна джоба из группы может исполняться в момент времени. 
# В примере - deploy-to-staging джобы из разных пайплайнов никогда не будут исполняться одновременно.	
deploy-to-staging:
  script: deploy
  resource_group: staging


# 20. [ retry ] 

# Указывает, сколько раз джоба повторит свое выполнение в случае падения
retry:when
	job:
  script: 
    retry: 
       max: 2
       when: specific_failure


# 21. [ rules ] 

# Позволяют включить/исключить джобы из пайплайна. 
# Rules не могут использоваться одновременно с only/except.
# rules:if
# rules:changes
# rules:changes:paths
# rules:changes:compare_to <branch>
# rules:exists <file_in_repo>
# rules:allow_failure
# rules:needs [‘needed_job_name’]
# rules:variables MY_VAR: “true”
job:
  script: <>
  rules:
    - if: $CI_MERGE_REQUEST_TARGET_BRANCH_NAME == $CI_DEFAULT_BRANCH
      when: manual
      allow_failure: true


# 22. [ script ] 

# Команды для выполнения на раннере.	
job:
  script: pytest


# 23. [ secrets ] 

# Позволяет указать секретные переменные от сторонних провайдеров
# secrets:vault
# secrets:azure_key_vault
# secrets:file
# secrets:token
job:
  secrets:
    MY_SECRET_VAR:
      azure_key_vault:
        name: <>
        version: <>


# 24. [ services ] 

# Позволяет указать дополнительные Docker images, которые необходимы скриптам для успешного выполнения
service:pull_policy
	job:
  script: <>
  services:
    - name: postgres:10.5
      pull_policy: always                                
      command: ["start"]


# 25. [ stage ] 

# Позволяет указать, к какому стейджу относится джоба 
stage: .pre
stage: .post

job:
  stage: .pre
  script:
    - echo “First job”


# 26. [ tags ] 

# Позволяет выбрать runner	  
tags:
    - hp-build


# 27. [ timeout ] 

# Указывает таймаут. Если джоба длится дольше таймаута - она падает.	
test:
  script: pytest
  timeout: 1h 30m


# 28. [ trigger ] 

# Позволяет запустить дочерний пайплайн
# trigger:include
# trigger:project
# trigger:strategy
# trigger:forward
trigger_job:
  trigger:
    include: child-pipeline.yml
    strategy: depend
    forward:
       pipeline_variables: true


# 29. [ variables ] 

# Задает глобальные переменные и переменные уровня джобы.	
variables:
  SITE: "https://smartiqa.ru/"


# 30. [ when ] 

# Указывает условия, при которых джоба будет запущена. Варианты: 
# on_success (default, джобы будет запущена, только если все джобы на предыдущих стейджах были успешны)
# on_failure
# never
# always (запустится вне зависимости от того, как прошли другие джобы)
# manual
# delayed	
job:
  stage: build
  script: <>

cleanup:
  stage: cleanup
  script:
    - <>
  when: on_failure


# 31. [ hooks ] 

# Используется, чтобы выполнить команды на определенных стадиях выполнения джобы.
# hooks:pre_get_sources_script
job:
  hooks:
    pre_get_sources_script:
      - <>
  script: <>


# 32. [ id_tokens ] 

# Используется для создания JSON Web Token (JWT)
job:
  id_tokens:
    ID_TOKEN:
      aud: https://aws.com
  script:
    - cmd_to_auth_with_aws $ID_TOKEN

```
###
3. Примеры переменных окружения / конфигов
Пример

#### 3.1. Значения переменных окружения

```
CI_PROJECT_NAMESPACE  =  smartiqa/tests
GITLAB_USER_ID  =  337
CI_RUNNER_VERSION  =  13.6.0
FF_SKIP_NOOP_BUILD_STAGES  =  true
CI_SERVER_NAME  =  GitLab
CI_RUNNER_DESCRIPTION  =  test-13.smart (docker)
GITLAB_USER_EMAIL  =  i.ivanov@smartiqa.ru
CI_SERVER_REVISION  =  9544e5451d7
CI_RUNNER_EXECUTABLE_ARCH  =  linux/amd64
CI_REGISTRY_USER  =  gitlab-ci-token
CI_API_V4_URL  =  https://gitlab.smartiqa.ru/api/v4
CI_REGISTRY_PASSWORD  =  [MASKED]
CI_RUNNER_SHORT_TOKEN  =  BZMFTyky
CI_JOB_NAME  =  flake8-check
HOSTNAME  =  runner-bzmftyky-project-344-concurrent-0
PYTHON_VERSION  =  3.9.18
GITLAB_USER_LOGIN  =  i.ivanov
CI_PROJECT_NAME  =  smartiqa-auto-testing
CI_PIPELINE_SOURCE  =  push
CI_JOB_STATUS  =  running
FF_SHELL_EXECUTOR_USE_LEGACY_PROCESS_KILL  =  false
CI_PIPELINE_ID  =  441438
CI_COMMIT_REF_SLUG  =  iivanov-samples
CI_SERVER  =  yes
FF_USE_GO_CLOUD_WITH_CACHE_ARCHIVER  =  true
CI_COMMIT_SHORT_SHA  =  fd6e0d96
CI_JOB_NAME_SLUG  =  flake8-check
FF_CMD_DISABLE_DELAYED_ERROR_LEVEL_EXPANSION  =  false
CI_DEPENDENCY_PROXY_GROUP_IMAGE_PREFIX  =  gitlab.smartiqa.ru:443/smartiqa/dependency_proxy/containers
PWD  =  /builds/smartiqa/tests/smartiqa-auto-testing
CI_RUNNER_TAGS  =  ["smartiqa-build"]
CI_PROJECT_PATH  =  endpoint/tests/smartiqa-auto-testing
MONITORING_SLACK_URL  =  [MASKED]
LINUX_PASS  =  [MASKED]
CI_SERVER_TLS_CA_FILE  =  /builds/smartiqa/tests/smartiqa-auto-testing.tmp/CI_SERVER_TLS_CA_FILE
CI_DEPENDENCY_PROXY_DIRECT_GROUP_IMAGE_PREFIX  =  gitlab.smartiqa.ru:443/endpoint/tests/dependency_proxy/containers
PYTHON_SETUPTOOLS_VERSION  =  58.1.0
ACCESS_TOKEN  =  [MASKED]
FF_RESET_HELPER_IMAGE_ENTRYPOINT  =  true
CI_COMMIT_REF_PROTECTED  =  false
CI_API_GRAPHQL_URL  =  https://smartiqa.ru/api/graphql
CI_SERVER_VERSION_MINOR  =  2
CI_COMMIT_SHA  =  fd6e0d964e7e83a89e4250eb78aebdca214c33e2
HOME  =  /root
FF_NETWORK_PER_BUILD  =  false
LANG  =  C.UTF-8
CI_DEPENDENCY_PROXY_PASSWORD  =  [MASKED]
CI_PROJECT_VISIBILITY  =  private
CI_CONCURRENT_PROJECT_ID  =  0
CI_COMMIT_MESSAGE  =  Updated Testrail link + Docker image
CI_SERVER_SHELL_SSH_PORT  =  22
CI_JOB_JWT_V1  =  [MASKED]
CI_JOB_JWT_V2  =  [MASKED]
FF_USE_DIRECT_DOWNLOAD  =  true
CI_PAGES_DOMAIN  =  smartiqa.ru
CI_SERVER_VERSION  =  16.2.4-ee
GPG_KEY  =  E3FF2839C048B25C084DEBE9B26995E310250568
CI_REGISTRY  =  gitlab.smartiqa.ru:4567
CI_SERVER_PORT  =  443
CI_PROJECT_NAMESPACE_ID  =  1310
NEXUS_IQ_CREDS  =  [MASKED]
CI_PAGES_URL  =  https://smartiqa.ru/tests/smartiqa-auto-testing
CI_PIPELINE_IID  =  6030
CI_REPOSITORY_URL  =  https://gitlab-ci-token:[MASKED]@gitlab.smartiqa.ru/smartiqa/tests/smartiqa-auto-testing.git
CI_SERVER_URL  =  https://gitlab.smartiqa.ru
GITLAB_FEATURES  =  audit_events,blocked_issues,board_iteration_lists,code_owners,code_review_analytics,contribution_analytics,elastic_search,full_codequality_report,group_activity_analytics,group_bulk_edit,group_webhooks,issuable_default_templates,issue_weights,iterations,ldap_group_sync,member_lock,merge_request_approvers,milestone_charts,multiple_issue_assignees,multiple_ldap_servers,multiple_merge_request_assignees,multiple_merge_request_reviewers,project_merge_request_analytics,protected_refs_for_users,push_rules,repository_mirrors,resource_access_token,seat_link,usage_quotas,visual_review_app,wip_limits,zoekt_code_search,description_diffs,send_emails_from_admin_area,repository_size_limit,maintenance_mode,scoped_issue_board,adjourned_deletion_for_projects_and_groups,admin_audit_log,auditor_user,blocking_merge_requests,board_assignee_lists,board_milestone_lists,ci_cd_projects,ci_secrets_management,cluster_agents_ci_impersonation,cluster_agents_user_impersonation,cluster_deployments,code_owner_approval_required,commit_committer_check,commit_committer_name_check,compliance_framework,custom_compliance_frameworks,cross_project_pipelines,custom_file_templates,custom_file_templates_for_namespace,custom_project_templates,cycle_analytics_for_groups,cycle_analytics_for_projects,db_load_balancing,default_branch_protection_restriction_in_groups,default_project_deletion_protection,delete_unconfirmed_users,dependency_proxy_for_packages,disable_name_update_for_users,disable_personal_access_tokens,domain_verification,email_additional_text,epics,extended_audit_events,external_authorization_service_api_management,feature_flags_related_issues,feature_flags_code_references,file_locks,geo,generic_alert_fingerprinting,git_two_factor_enforcement,github_integration,group_allowed_email_domains,group_coverage_reports,group_forking_protection,group_milestone_project_releases,group_project_templates,group_repository_analytics,group_saml,group_scoped_ci_variables,group_wikis,ide_schema_config,incident_metric_upload,incident_sla,instance_level_scim,issues_analytics,jira_issues_integration,ldap_group_sync_filter,merge_pipelines,merge_request_performance_metrics,admin_merge_request_approvers_rules,merge_trains,metrics_reports,multiple_alert_http_integrations,multiple_approval_rules,multiple_group_issue_boards,object_storage,microsoft_group_sync,operations_dashboard,package_forwarding,pages_size_limit,productivity_analytics,project_aliases,protected_environments,reject_non_dco_commits,reject_unsigned_commits,remote_development,saml_group_sync,service_accounts,scoped_labels,smartcard_auth,swimlanes,type_of_work_analytics,minimal_access_role,unprotection_restrictions,ci_project_subscriptions,incident_timeline_view,oncall_schedules,escalation_policies,export_user_permissions,zentao_issues_integration,coverage_check_approval_rule,issuable_resource_links,group_protected_branches,group_level_merge_checks_setting,oidc_client_groups_claim,disable_deleting_account_for_users,group_ip_restriction,password_complexity
NEXUS_IQ_URL  =  [MASKED]
CI_COMMIT_DESCRIPTION  =  
CI_TEMPLATE_REGISTRY_HOST  =  registry.gitlab.com
CI_JOB_STAGE  =  style_checks
CI_PIPELINE_URL  =  https://gitlab.smartiqa.ru/smartiqa/tests/smartiqa-auto-testing/-/pipelines/441438
CI_DEFAULT_BRANCH  =  master
PYTHONPATH  =  /opt/app
CI_SERVER_VERSION_PATCH  =  4
CI_COMMIT_TITLE  =  Updated Testrail link + Docker image
CI_PROJECT_ROOT_NAMESPACE  =  endpoint
GITLAB_USER_NAME  =  Ivan Ivanov
CI_PROJECT_DIR  =  /builds/smartiqa/tests/smartiqa-auto-testing
SHLVL  =  1
CI_RUNNER_ID  =  63
CI_PIPELINE_CREATED_AT  =  2023-09-04T12:57:31Z
CI_COMMIT_TIMESTAMP  =  2023-09-04T15:57:25+03:00
CI_DISPOSABLE_ENVIRONMENT  =  true
CI_SERVER_SHELL_SSH_HOST  =  gitlab.smartiqa.ru
CI_JOB_JWT  =  [MASKED]
CI_REGISTRY_IMAGE  =  gitlab.smartiqa.ru:4567/smartiqa/tests/smartiqa-auto-testing
CI_SERVER_PROTOCOL  =  https
PYTHON_PIP_VERSION  =  23.0.1
CI_COMMIT_AUTHOR  =  Ivan Ivanov <i.ivanov@smartiqa.ru>
CI_COMMIT_REF_NAME  =  iivanov/samples
CI_SERVER_HOST  =  gitlab.smartiqa.ru
CI_JOB_URL  =  https://gitlab.smartiqa.ru/smartiqa/tests/smartiqa-auto-testing/-/jobs/2711509
CI_JOB_TOKEN  =  [MASKED]
CI_JOB_STARTED_AT  =  2023-09-04T12:57:33Z
CI_CONCURRENT_ID  =  0
CI_PROJECT_DESCRIPTION  =  
CI_COMMIT_BRANCH  =  iivanov/samples
CI_PROJECT_CLASSIFICATION_LABEL  =  
FF_USE_LEGACY_KUBERNETES_EXECUTION_STRATEGY  =  true
CI_RUNNER_REVISION  =  8fa89735
PYTHON_GET_PIP_SHA256  =  45a2bb8bf2bb5eff16fdd00faef6f29731831c7c59bd9fc2bf1f3bed511ff1fe
CI_DEPENDENCY_PROXY_USER  =  gitlab-ci-token
CI_PROJECT_PATH_SLUG  =  smartiqa-tests-smartiqa-auto-testing
CI_NODE_TOTAL  =  1
CI_BUILDS_DIR  =  /builds
CI_JOB_ID  =  2711509
CI_PROJECT_REPOSITORY_LANGUAGES  =  python,go,groovy,c++,c
PYTHON_GET_PIP_URL  =  https://github.com/pypa/get-pip/raw/9af82b715db434abb94a0a6f3569f43e72157346/public/get-pip.py
PATH  =  /usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
CI_PROJECT_ID  =  344
CI  =  true
GITLAB_CI  =  true
CI_JOB_IMAGE  =  gitlab.smartiqa.ru:4567/lib/autotest_utils/runner:latest
VCLOUD_TOKEN  =  [MASKED]
CI_COMMIT_BEFORE_SHA  =  b319bdf4874efada3b5da7f7264eff62b5157dab
CI_PROJECT_TITLE  =  smartiqa-auto-testing
CI_SERVER_VERSION_MAJOR  =  16
UNSTABLE  =  1
CI_CONFIG_PATH  =  .gitlab-ci.yml
FF_USE_FASTZIP  =  false
CI_DEPENDENCY_PROXY_SERVER  =  gitlab.smartiqa.ru:443
CI_PROJECT_URL  =  https://gitlab.smartiqa.ru/smartiqa/tests/smartiqa-auto-testing
OLDPWD  =  /opt/app
_  =  /usr/bin/printenv

```
#### Пример 3.2. Конфиг .gitlab-ci.yml

```
include:
  - project: smartiqa-infra/ci-cd
    file:
      - templates-build.yml
      - templates-upload.yml
stages:
  - build

compile_go:
  stage: build
  extends: .build-binary-go-current
  variables:
    GOPRIVATE: "gitlab.smartiqa.ru/ax/dparser"
    GIT_TERMINAL_PROMPT: "1"
    GOSUMDB: "off"
    GOOS: "windows"
    GOARCH: "amd64"
  script:
    - go build -o dparser main.go
    - ls
  artifacts:
    paths:
      - dparser

upload_new_version:
  stage: .post
  image: ${CI_REGISTRY}/smartiqa-infra/docker-images/common:curl
  script:
    - curl -XPUT -u dev_user:WHhW9GqNeNtw8ytft https://download.smartiqa.ru/parser/${CI_COMMIT_TAG}/dparser.exe --upload-file dparser
    - sshpass -p <pwd> scp -o StrictHostKeyChecking=no dparser dev_user@172.18.11.4:parse\\dparser.exe
    - curl --location --request POST 'https://smartiqa.ru/api/send/alert' --header 'Content-Type:application/json' -d '{"to":[], "body":"New dparser version:'${CI_COMMIT_TAG}'", "channelId":"C04FPKL3VUY"}'
  rules:
    - if: '$CI_COMMIT_TAG'

```
