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
