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
