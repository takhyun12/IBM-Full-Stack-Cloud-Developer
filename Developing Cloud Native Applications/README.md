# Developing Cloud Native Applications


Certificate of the course that is offered at Coursera and IBM.

#### Author: Tackhyun Jung

#### Status: Completed

This repository is created to keep track of [Developing Cloud Native Applications](https://www.coursera.org/learn/developing-cloud-native-applications) provided by Coursera.
This educational program is developed by IBM and designed to teach how to program in cloud computing environment.

## Learning Objectives

- Introduction to Cloud Native `week 1`
- Getting Started with IBM Cloud `week 2`
- IBM Cloud CLI `week 3`
- DevOps on IBM Cloud `week 4`
- REST Architecture and Watson API `week 5`
- Introduction to Data Services in IBM Cloud `week 6`
- Final Project `week 7`

## Assignment
IBM provides a Continuous Delivery service along with an integrated set of tools to build, deploy and manage your applications. Continuous Delivery automatically runs the build and deploy tasks when you commit changes to the Git repository (repo). 

I developed CI/CD Pipeline as a challenge through Continuous Delivery from IBM.

![CICD](https://user-images.githubusercontent.com/41291493/110789769-97a71b00-82b3-11eb-8484-e33299e7c312.png)

## Note

```
1) 클라우드 네이티브 애플리케이션
클라우드 네이티브 애플리케이션은 탄력적으로 결합된 소규모의 독립적인 서비스 컬렉션이다. 
다시 말해, 새로운 애플리케이션을 구축하고, 기존 애플리케이션을 최적화하고, 모든 환경을 연결하는 작업을 가속화할 수 있는 방법이다.

2) 클라우드 네이티브 애플리케이션을 어떻게 구축할까요?
클라우드 네이티브 애플리케이션은 조직 내 인력과 이들의 협업 프로세스를 자동화하는 것에서 시작합니다.

컨테이너를 도입하면 이상적인 애플리케이션 배포 유닛 및 독립적인 실행 환경을 제공하여 이러한 프랙티스를 지원할 수 있다.
DevOps 및 컨테이너 접근 방식에서는 하나의 대규모 릴리스 및 업데이트를 기다리는 것이 아니라 마이크로서비스처럼 여러 서비스가 탄력적으로 결합된 하나의 컬렉션으로 애플리케이션을 쉽게 출시 및 업데이트한다.

클라우드 네이티브 개발은 아키텍처의 모듈성, 탄력적인 결합, 독립적인 서비스에 중점을 둔다.
각 마이크로서비스는 비즈니스 역량을 구현하고 자체 프로세스를 실행하고 애플리케이션 프로그래밍 인터페이스(Application Programming Interfaces, API) 또는 메시징을 통해 커뮤니케이션한다.
이러한 커뮤니케이션은 서비스 메쉬 레이어를 통해 관리할 수 있다.

기존 조직의 아키텍처를 이용하여 계속해서 레거시 애플리케이션을 최적화할 수 있다. 
이러한 최적화는 지속적인 통합(Continuous Integration, CI)과 지속적인 제공(Continuous Delivery, CD) 및 완전히 자동화된 배포 운영 같은 DevOps 워크플로우를 통해 지원된다.

3) DevOps 
DevOps는 하나의 아이디어(기능 개발, 버그 수정 등)가 사용자에게 가치를 제공할 수 있도록 운영 환경에서 개발로부터 배포로 진행되는 프로세스의 속도를 높이는 접근 방식을 의미한다.
DevOps를 확립하면 셀프 서비스와 자동화를 통해 다양한 이점과 경쟁력을 얻을 수 있다.
이는 곧 코드 변경도 더 빈번해지고 인프라도 보다 역동적으로 사용해야 한다는 의미이다.

4) 마이크로서비스(Microservices)
마이크로서비스란 소프트웨어를 구축하기 위한 아키텍처이자 하나의 접근 방식으로, 애플리케이션을 상호 독립적인 최소 구성 요소로 분할한다.
마이크로서비스에서는 모든 요소가 독립적이며 연동되어 동일한 태스크를 완수한다.

마이크로서비스는 분산형 개발을 통해 팀의 역량과 일상적인 업무 능력을 향상시킨다.
또한, 동시에 여러 마이크로서비스를 개발하는 것도 가능합니다. 다시 말해, 동일한 애플리케이션 개발에 더 많은 개발자들이 동시 참여할 수 있으므로 개발에 소요되는 시간을 단축할 수 있다.

마이크로 서비스는 개발주기 단출, 높은 확장성, 뛰어난 복구 능력, 손쉬운 배포, 편리한 엑세스, 향상된 개발성 등 다양한 강점이 존재한다.

5) API
애플리케이션 프로그래밍 인터페이스(Application Programming Interfaces, API)는 애플리케이션 소프트웨어 및 서비스를 통합하는 툴, 정의, 프로토콜이다. 
이는 새로운 연결 인프라를 지속적으로 구축할 필요 없이 제품 및 서비스가 서로 커뮤니케이션할 수 있도록 도와주는 기능이다.

SOAP(Simple Object Access Protocol) 및 REST(Representational State Transfer)는 API의 설계 편의성과 구현 유용성을 높이기 위해 사용되었다.
웹 API가 널리 사용되면서, 메시지 형식 및 요청을 표준화하기 위해 SOAP라는 프로토콜 사양이 개발되었다.

6) 컨테이너
Linux 컨테이너는 실행에 필요한 모든 파일을 포함하여 전체 런타임 환경에서 애플리케이션을 패키지화하고 분리하는 기술이다.
이를 통해 전체 기능을 유지하면서 컨테이너화된 애플리케이션을 환경(개발, 테스트, 생산 등) 간에 쉽게 이동할 수 있다.

컨테이너는 규모에 관계없이 다양한 워크로드 및 활용 사례에 배포할 수 있다.
컨테이너는 클라우드 네이티브 개발 방식에 필요한 기반 기술을 제공하므로 이를 통해 개발자는 DevOps, CI/CD(지속적인 통합 및 지속적인 배포)를 시작할 수 있으며 서버리스(serverless)로 전환할 수 있다.

7) 서버리스(serverless) 
서버리스(serverless)란 개발자가 서버를 관리할 필요 없이 애플리케이션을 빌드하고 실행할 수 있도록 하는 클라우드 네이티브 개발 모델이다.
서버리스 모델에도 서버가 존재하긴 하지만, 애플리케이션 개발에서와 달리 추상화되어 있다. 
클라우드 제공업체가 서버 인프라에 대한 프로비저닝, 유지 관리, 스케일링 등의 일상적인 작업을 처리하며, 개발자는 배포를 위해 코드를 컨테이너에 패키징하기만 하면 된다.

BaaS (Backend as a Service)
앱 개발에 있어서 필요한 다양한 기능들 (데이터베이스, 소셜서비스 연동, 파일시스템 등)을 API로 제공해 줌으로서, 개발자들이 서버 개발을 하지 않고서도 필요한 기능을 쉽고 빠르게 구현 할 수 있게 해주고, 
비용은 사용 한 만큼 지불하게 되는 방식을 말한다. 가장 대표적으로는 Firebase를 많이 사용한다.

장점 : 개발 시간의 단축 (회사 입장으로서 생각한다면, 인건비), 서버 확장 작업의 불필요 
단점 : 백엔드 로직들이 클라이언트쪽에 구현이 됨, 가격이 비쌈

FaaS (Function as a Service)
FaaS 는 프로젝트를 여러개의 함수로 쪼개서 (혹은 한개의 함수로 만들어서), 매우 거대하고 분산된 컴퓨팅 자원에 여러분이 준비해둔 함수를 등록하고, 
이 함수들이 실행되는 횟수 (그리고 실행된 시간) 만큼 비용을 내는 방식을 말한다.

장점 : 함수 호출단위로 비용을 청구하기 때문에 가격이 저렴함, 인프라 관리를 하지 않아도 됨
단점 : 함수로 사용할 수 있는 자원(컴퓨팅 파워)에 제한이 있음, Faas 제공사에 종속됨

8) CI / CD
CI/CD는 애플리케이션 개발 단계를 자동화하여 애플리케이션을 보다 짧은 주기로 고객에게 제공하는 방법임
CI/CD의 기본 개념은 지속적인 통합, 지속적인 서비스 제공, 지속적인 배포이다

개발자의 변경 사항을 Repository에서 고객이 사용 가능한 프로덕션 환경까지 자동으로 릴리스하는 것을 의미함
CI(지속적 통합)를 통해 개발자들은 코드 변경 사항을 공유 브랜치 또는 "트렁크"로 다시 병합하는 작업을 더욱 수월하게 자주 수행할 수 있음

지속적 통합 / 지속적 제공 / 지속적 배포의 단계로 수행됨
```

## Credit

- [Introduction to Cloud Computing](https://www.coursera.org/learn/introduction-to-cloud)
- [Certification-Link](https://www.coursera.org/account/accomplishments/verify/ARUZJ5MFXRY7)
