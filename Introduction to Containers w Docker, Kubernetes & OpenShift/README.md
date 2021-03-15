# Introduction to Containers w Docker, Kubernetes & OpenShift

Certificate of the course that is offered at Coursera and IBM.

#### Author: Tackhyun Jung

#### Status: Completed

This repository is created to keep track of [Introduction to Containers w/ Docker, Kubernetes & OpenShift](https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift?) provided by Coursera.
This educational program is developed by IBM and designed to teach how to program in cloud computing environment.

![Certification](https://user-images.githubusercontent.com/41291493/111091172-6b222600-8575-11eb-874b-cf29cb272508.png)

## Learning Objectives

- Understanding the Benefits of Containers `week 1`
- Understanding Kubernetes Architecture `week 2`
- Managing Applications with Kubernetes `week 3`
- The Kubernetes Ecosystem: OpenShift, Istio, etc. `week 4`
- Final Assignment `week 5`

## Assignment
This final assignment is a project that use many of the tools and concepts that I've learned so far in this course. This project is conducted on an OpenShift cluster.

First of all, I did deploy a simple guestbook application that uses in-memory storage to retain the guestbook entries. 

Afterward, I did deploy a multi-tier web application that consists of a web front end, a Redis master and replicated slaves for storage, as well as an analyzer service that analyzes the tone of entries left in the guestbook. 

After development, I used docker, Kubernetes through OpenShift cluster.

![web](https://user-images.githubusercontent.com/41291493/111073218-456b3180-8521-11eb-8a11-833b56628860.png)

![pod](https://user-images.githubusercontent.com/41291493/111073216-44d29b00-8521-11eb-9aeb-fe03e648b52a.png)

## Note

```
1) Containers
컨테이너는 애플리케이션을 실제 구동 환경으로부터 추상화할 수 있는 논리 패키징 메커니즘을 제공합니다. 
이러한 분리를 통해 사설 데이터 센터나 퍼블릭 클라우드, 심지어 개발자의 개인 노트북 컴퓨터에 이르기까지
어떤 환경으로든 컨테이너 기반 애플리케이션을 쉽게 지속적으로 배포할 수 있습니다.

또한 컨테이너화를 통해 업무 영역을 깔끔하게 분리할 수 있습니다. 
즉, 개발자는 애플리케이션의 로직과 종속 항목에만 집중하고,
IT 운영팀은 특정 소프트웨어 버전, 개별 앱 구성과 관련한 세부 업무에 시간을 낭비하지 않고 배포 및 관리에 집중할 수 있습니다.

가상 머신(VM)은 하드웨어 스택을 가상화합니다. 
컨테이너는 이와 달리 운영체제 수준에서 가상화를 실시하여 다수의 컨테이너를 OS 커널에서 직접 구동합니다.
이러한 원리에 따라 컨테이너는 훨씬 가볍고 OS 커널을 공유하며, 시작이 훨씬 빠르고 OS 전체 부팅보다 메모리를 훨씬 적게 차지합니다.

2) Docker
Docker는 애플리케이션을 신속하게 구축, 테스트 및 배포할 수 있는 소프트웨어 플랫폼입니다.
Docker는 소프트웨어를 컨테이너라는 표준화된 유닛으로 패키징하며, 
이 컨테이너에는 라이브러리, 시스템 도구, 코드, 런타임 등 소프트웨어를 실행하는 데 필요한 모든 것이 포함되어 있습니다.

3) Kubernetes
'k8s'라고도 불리는 Kubernetes는 머신 및 서비스 관리를 대행하는 자동화된 컨테이너 조정 기능을 제공합니다. 
이에 따라 안정성이 높아지고 관리 작업의 부담이 해소될 뿐만 아니라 DevOps에 써야 하는 시간과 리소스도 절감됩니다.

Kubernetes를 사용하면 애플리케이션의 배포 및 관리와 관련된 모든 작업이 한층 간편해집니다.
Kubernetes는 출시 및 롤백을 자동화하고 서비스 상태를 모니터링하여 상황이 악화되기 전에 불량 버전 출시를 예방합니다.
또한 끊임없이 서비스 상태를 확인하여 오류가 발생하거나 중단된 컨테이너를 재시작하며, 사용률에 따라 자동으로 서비스의 규모를 조절합니다.
컨테이너와 마찬가지로 Kubernetes를 사용하면 선언형으로 클러스터를 관리하여 더욱 손쉽게 버전을 제어하고 복제할 수 있습니다.

4) OpenShift
Red Hat OpenShift®는 자동화된 풀스택 오퍼레이션으로 하이브리드 클라우드 및 멀티클라우드 배포를 관리하는 쿠버네티스, 컨테이너 플랫폼입니다.

Red Hat OpenShift는 강력한 컨테이너 클러스터 관리 및 Docker와 Kubernetes와 같은 기술을 기본적으로 통합하고,
이를 Red Hat Enterprise Linux에서 엔터프라이즈 기반에 결합하는 전체 컨테이너 애플리케이션 플랫폼입니다.

이러한 Red Hat OpenShift 기반의 Red Hat Middleware는 모든 환경과 애플리케이션 라이프사이클 전반에 걸쳐 클라우드 네이티브 애플리케이션을
배포, 제공, 확장할 수 있도록 일관되고 통합된 환경을 제공합니다. 

6) IStio
Istio는 플랫폼, 소스 또는 공급업체와 무관하게 개발자가 다양한 마이크로서비스의 네트워크를 완벽하게 연결, 관리할 수 있는 개방형 기술입니다.
Istio는 Istio를 Kubernetes 클러스터와 직접 통합하는 관리형 추가 기능으로 제공됩니다.
단 한 번의 클릭으로 튜닝된 프로덕션용 Istio 인스턴스를 IBM Cloud Kubernetes Service 클러스터에 배치할 수 있습니다.
```

## Credit

- [Introduction to Containers w/ Docker, Kubernetes & OpenShift](https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift?)
- [Certification-Link]
