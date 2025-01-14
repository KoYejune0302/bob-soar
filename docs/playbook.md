# Playbook: 이상 IP 탐지 및 분석 자동화

## **1. 개요**

- **목적**: 이상 IP 접근이 탐지되면 TheHive에서 자동으로 사례(Case)와 작업(Task)를 생성하고, Observable을 통해 다양한 분석 도구(ThreatMiner, TorProject, Urlscan.io, VirusTotal)를 활용하여 IP를 분석한 후, 이상 IP인 경우 접근을 차단하고 보고서를 생성한다.

---

## **2. Playbook 단계**

### **2.1. TheHive에서 사례 생성**

- **조건**: 이상 IP 접근 탐지
- **동작**:
  - TheHive에서 새로운 사례 생성
  - 작업(Task) 자동 할당

### **2.2. Cortex를 통한 IP 분석**

- **조건**: 사례 생성 완료
- **동작**:
  - Cortex 분석기 실행 (ThreatMiner, TorProject, Urlscan.io, VirusTotal)
  - 분석 결과 수집

### **2.3. 분석 결과 검토**

- **조건**: 분석 완료
- **동작**:
  - 분석 결과를 바탕으로 이상 IP 여부 판단
  - 이상 IP인 경우 작업 4로 이동

### **2.4. 접근 차단**

- **조건**: 이상 IP 판단
- **동작**:
  - 방화벽 또는 IPS에서 해당 IP 차단

### **2.5. 보고서 생성**

- **조건**: 모든 작업 완료
- **동작**:
  - 분석 결과 및 조치 사항을 포함한 보고서 생성
  - 보고서를 TheHive에 첨부

---

## **3. 시나리오 흐름**

1. **이상 IP 접근 탐지**
2. **TheHive에서 사례 및 작업 생성**
3. **Cortex를 통한 IP 분석**
4. **분석 결과 검토**
5. **이상 IP인 경우 접근 차단**
6. **보고서 생성**