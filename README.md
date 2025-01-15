# SOAR

TheHive + Cortex + Python

## Install

`https://docs.strangebee.com/thehive/installation/docker/`

### 환경 설정

[Settings](./docs/settings.md "Settings")

## Scenario - [mermaid](./docs/scenario.md "Flow Chart")

![Flow Chart](./images/scenario.png "Flow Chart")

1. 이상 IP 접근 탐지

2. TheHive에서 사례 및 작업 생성

3. Cortex를 통한 IP 분석

4. 분석 결과 검토

5. 이상 IP인 경우 접근 차단

6. 보고서 생성

## Workbook

[Workbook](./docs/workbook.md "Workbook")

## Playbook

[Playbook](./docs/playbook.md "Playbook")

## Flow Analysis

### IP 접근

![Flask](./images/flask_1.png "Flask")
IP 접근을 테스트 하기 위해 Flask를 이용해 간단한 web browser를 구현한다.

### 이상 IP 접근

![Flask Code](./images/flask_code.png "Flask Code")
![Flask](./images/flask_2.png "Flask")
이상 IP가 접근했다고 가정하고 해당 접근에 대한 Case를 생성한다.<br>

### Case 생성 자동화

![Code](./images/thehive_code.png "Code")
![Case](./images/thehive_case.png "Case")
TheHive API를 이용하여 case 생성

### Task 생성

![Task](./images/thehive_task.png "Task")
TheHive API를 이용하여 Task 생성

### Observable 생성

![Observable](./images/thehive_observable.png "Observable")
TheHive API를 이용하여 각 IP 마다 Observable 생성

### (TODO) Analyzer

![Analyzer](./images/thehive_analyzer.png "Analyzer")
![Jobs](./images/cortex_test.png "Cortex Test")
Cortex를 이용하여 분석을 진행하고 결과를 확인

### (TODO) Alert 생성

TODO: TheHive Alert를 생성하고 해당 보고서를 메일로 전송하는 기능 구현
