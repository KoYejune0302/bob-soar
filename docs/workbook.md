# Workbook: 이상 IP 접근 탐지 및 분석

## **1. 개요**

- **목적**: 이상 IP 접근이 탐지되면 TheHive에서 자동으로 사례(Case)와 작업(Task)를 생성하고, Observable을 통해 다양한 분석 도구(ThreatMiner, TorProject, Urlscan.io, VirusTotal, AbuseIPDB)를 활용하여 IP를 분석한 후, 이상 IP인 경우 접근을 차단하고 보고서를 생성한다.

---

## **2. Case 생성**

### **2.1. 사례 제목**

- **이상 IP 접근 탐지 및 분석**

### **2.2. 사례 설명**

- **설명**: 이상 IP로부터의 접근이 탐지되었습니다. 해당 IP에 대한 분석을 수행하고, 이상 여부를 판단하여 접근 차단 및 보고서를 생성합니다.

### **2.3. 태그**

- `이상 IP`, `자동 분석`, `보고서`

### **2.4. 작업(Task) 목록**

1. **IP 분석 시작**
   - Cortex를 통해 ThreatMiner, TorProject, Urlscan.io, VirusTotal, AbuseIPDB 분석 실행
2. **분석 결과 검토**
   - 분석 결과를 바탕으로 이상 IP 여부 판단
3. **접근 차단**
   - 이상 IP인 경우 방화벽 또는 IPS에서 해당 IP 차단
4. **보고서 생성**
   - 분석 결과 및 조치 사항을 포함한 보고서 작성

---

## **3. Task 생성**

### **3.1. 작업 1: IP 분석 시작**

- **설명**: Cortex를 통해 ThreatMiner, TorProject, Urlscan.io, VirusTotal, AbuseIPDB를 사용하여 IP 분석을 시작합니다.
- **Cortex 분석기**:
  - ThreatMiner: IP와 관련된 도메인, 파일 해시 정보 수집
  - TorProject: Tor 네트워크 사용 여부 확인
  - Urlscan.io: IP와 관련된 URL 스캔
  - VirusTotal: 악성 IP 여부 확인
  - AbuseIPDB: 악성 IP 여부 확인

### **3.2. 작업 2: 분석 결과 검토**

- **설명**: 분석 결과를 바탕으로 이상 IP 여부를 판단합니다.
- **판단 기준**:
  - ThreatMiner: 악성 도메인 또는 파일 해시 발견
  - TorProject: Tor 네트워크 사용
  - Urlscan.io: 악성 URL 발견
  - VirusTotal: 악성 IP로 분류
  - AbuseIPDB: 악성 IP로 분류

### **3.3. 작업 3: 접근 차단**

- **설명**: 이상 IP인 경우 방화벽 또는 IPS에서 해당 IP를 차단합니다.
- **조치 사항**:
  - 방화벽 규칙 추가
  - IPS에서 차단 정책 적용

### **3.4. 작업 4: 보고서 생성**

- **설명**: 분석 결과 및 조치 사항을 포함한 보고서를 작성합니다.
- **보고서 항목**:
  - 분석 도구별 결과
  - 이상 IP 여부
  - 차단 조치 사항

---

## **4. MITRE ATT&CK 매핑**

| **단계**              | **ATT&CK Tactic**        | **ATT&CK Technique** |
| --------------------- | ------------------------ | -------------------- |
| 이상 IP 접근 탐지     | Initial Access (TA0001)  | T1078, T1190         |
| TheHive에서 사례 생성 | None                     | None                 |
| Cortex를 통한 IP 분석 | Discovery (TA0007)       | T1046                |
| 분석 결과 검토        | None                     | None                 |
| 접근 차단             | Defense Evasion (TA0005) | T1089                |
| 보고서 생성           | None                     | None                 |

---

## **5. 참조 링크**

- [Initial Access (TA0001)](https://attack.mitre.org/tactics/TA0001/)
- [Discovery (TA0007)](https://attack.mitre.org/tactics/TA0007/)
- [Defense Evasion (TA0005)](https://attack.mitre.org/tactics/TA0005/)
