# Workbook

- 보안 이슈에 대한 대응 작업을 문서화한 것

## Case 생성

### 사례 제목

- **이상 IP 접근 탐지 및 분석**

### 사례 설명

- **설명**: 이상 IP로부터의 접근이 탐지되었습니다. 해당 IP에 대한 분석을 수행하고, 이상 여부를 판단하여 접근 차단 및 보고서를 생성합니다.

### 태그

- `이상 IP`, `자동 분석`, `보고서`

### 작업(Task) 목록

1. **IP 분석 시작**
   - Cortex를 통해 ThreatMiner, TorProject, Urlscan.io, VirusTotal 분석 실행
2. **분석 결과 검토**
   - 분석 결과를 바탕으로 이상 IP 여부 판단
3. **접근 차단**
   - 이상 IP인 경우 방화벽 또는 IPS에서 해당 IP 차단
4. **보고서 생성**
   - 분석 결과 및 조치 사항을 포함한 보고서 작성

## Task 생성

### 작업 1: IP 분석 시작

- **설명**: Cortex를 통해 ThreatMiner, TorProject, Urlscan.io, VirusTotal을 사용하여 IP 분석을 시작합니다.
- **Cortex 분석기**:
  - ThreatMiner: IP와 관련된 도메인, 파일 해시 정보 수집
  - TorProject: Tor 네트워크 사용 여부 확인
  - Urlscan.io: IP와 관련된 URL 스캔
  - VirusTotal: 악성 IP 여부 확인

### 작업 2: 분석 결과 검토

- **설명**: 분석 결과를 바탕으로 이상 IP 여부를 판단합니다.
- **판단 기준**:
  - ThreatMiner: 악성 도메인 또는 파일 해시 발견
  - TorProject: Tor 네트워크 사용
  - Urlscan.io: 악성 URL 발견
  - VirusTotal: 악성 IP로 분류

### 작업 3: 접근 차단

- **설명**: 이상 IP인 경우 방화벽 또는 IPS에서 해당 IP를 차단합니다.
- **조치 사항**:
  - 방화벽 규칙 추가
  - IPS에서 차단 정책 적용

### 작업 4: 보고서 생성

- **설명**: 분석 결과 및 조치 사항을 포함한 보고서를 작성합니다.
- **보고서 항목**:
  - 분석 도구별 결과
  - 이상 IP 여부
  - 차단 조치 사항
