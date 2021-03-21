# Application Development using Microservices and Serverless

Certificate of the course that is offered at Coursera and IBM.

#### Author: Tackhyun Jung

#### Status: Completed

This repository is created to keep track of [Application Development using Microservices and Serverless](https://www.coursera.org/learn/applications-development-microservices-serverless-openshift) provided by Coursera.
This educational program is developed by IBM and designed to teach how to program in cloud computing environment.

## Learning Objectives

- Introduction to MicroServices `week 1`
- Introduction to Serverless `week 2`
- ORM: MicroServices w/ Serverless `week 3`
- OpenShift Essentials/Working with OpenShift and Istio `week 4`
- Final Project(Assignment) `week 5`

## Assignment

I did my serverless and microservices skills and put them into action in a project that combines these technologies into a single web application. I did create a serverless web application -- a simple guestbook website where users can post messages -- and I did host the website in two different ways.

Below is the architecture for one version which uses object storage to host the site's files.




## Note

```
1) Microservices
마이크로서비스란 소프트웨어를 구축하기 위한 아키텍처이자 하나의 접근 방식으로, 애플리케이션을 상호 독립적인 최소 구성 요소로 분할한다.
마이크로서비스에서는 모든 요소가 독립적이며 연동되어 동일한 태스크를 완수한다.

마이크로서비스는 분산형 개발을 통해 팀의 역량과 일상적인 업무 능력을 향상시킨다.
또한, 동시에 여러 마이크로서비스를 개발하는 것도 가능합니다. 
다시 말해, 동일한 애플리케이션 개발에 더 많은 개발자들이 동시 참여할 수 있으므로 개발에 소요되는 시간을 단축할 수 있다.

마이크로 서비스는 개발주기 단출, 높은 확장성, 뛰어난 복구 능력, 손쉬운 배포, 편리한 엑세스, 향상된 개발성 등 다양한 강점이 존재한다.

2) Microservices Patterns and Anti-Patterns
몇몇 사람은 빈약한 도메인 모델을 안티패턴이라고도 합니다. 이 모델은 실제로 구현하는 내용에 따라 달라집니다. 

설계한 마이크로 서비스가 충분히 단순하다면(예를 들어, CRUD 서비스) 빈약한 도메인 모델을 따르는 것은 안티패턴이 아닙니다. 
그러나 끊임없이 변화하는 비즈니스 규칙이 많은 마이크로 서비스 도메인의 복잡성을 해결해야 하는 경우 해당 모델은 안티패턴일 수 있습니다.

3) Serverless
서버리스(serverless)란 개발자가 서버를 관리할 필요 없이 애플리케이션을 빌드하고 실행할 수 있도록 하는 클라우드 네이티브 개발 모델이다.
서버리스 모델에도 서버가 존재하긴 하지만, 애플리케이션 개발에서와 달리 추상화되어 있다. 
클라우드 제공업체가 서버 인프라에 대한 프로비저닝, 유지 관리, 스케일링 등의 일상적인 작업을 처리하며, 개발자는 배포를 위해 코드를 컨테이너에 패키징하기만 하면 된다.

4) Serverless Pros and Cons
서버리스는 애플리케이션을 빌드하고 백엔드 디자인 하는 방법을 바꾸고 있다.
서버가 없는 백엔드(x), 직접 서버를 관리하지 않는 경우(o)

하지만 서버의 소프트웨어는 관리를 직접해줘야 한다.
ex) 업데이트, 보안, 데이터 백업 etc...

서버리스를 활용하면 백엔드를 서버에 올리는 것이 아니다.
서버리스에서는 백엔드를 작은 함수단으로 쪼개서 직접 관리하지 않는 서버로 올린다. 예를 들면 AWS lambda.

Pros
서버리스가 아닌 경우 서버는 24시간 돌아간다.
서버리스의 경우 업로드한 함수는 잠을 자고 있다.
리퀘스트가 오는 순간 AWS는 함수를 깨울 것이고 요청한 작업을 수행하고 다시 함수는 잠에 들거다. (비용이 저렴)

스테이트리스 함수(Stateless Functions)
함수는 일반적으로 상태가 저장되지 않는(stateless) 컨테이너에서 보안적으로 안전하게(거의) 실행됩니다. 
즉, 이벤트가 완료된 이후 한 참이 지난 응용 프로그램 서버에서 코드를 재실행하거나 이전 실행 컨텍스트를 사용하여 요청을 제공하는 코드를 실행시킬 수 없습니다. 

Cons
리퀘스트가 와서 함수를 깨우는데 아무래도 시간이 걸린다.
이러한 경우들 때문에 AWS 람다의 경우 어떤 함수가 자주 쓰이는지 파악을 해서 해당 함수는 아예 잠들지 않고 리퀘스트에 빨리 대응할 수 있도록 대기한다고 한다.

콜드 스타트(Cold Starts)
함수(Function)는 이벤트에 응답하도록 설정된 컨테이너 내부에서 실행되기 때문에 이벤트와 관련된 어느 정도의 대기 시간을 필요로합니다. 

5) Function as a Service
FaaS 는 프로젝트를 여러개의 함수로 쪼개서 (혹은 한개의 함수로 만들어서), 매우 거대하고 분산된 컴퓨팅 자원에 여러분이 준비해둔 함수를 등록하고, 
이 함수들이 실행되는 횟수 (그리고 실행된 시간) 만큼 비용을 내는 방식을 말한다.

장점 : 함수 호출단위로 비용을 청구하기 때문에 가격이 저렴함, 인프라 관리를 하지 않아도 됨
단점 : 함수로 사용할 수 있는 자원(컴퓨팅 파워)에 제한이 있음, Faas 제공사에 종속됨

6) OpenShift
Red Hat OpenShift®는 자동화된 풀스택 오퍼레이션으로 하이브리드 클라우드 및 멀티클라우드 배포를 관리하는 쿠버네티스, 컨테이너 플랫폼입니다.

Red Hat OpenShift는 강력한 컨테이너 클러스터 관리 및 Docker와 Kubernetes와 같은 기술을 기본적으로 통합하고,
이를 Red Hat Enterprise Linux에서 엔터프라이즈 기반에 결합하는 전체 컨테이너 애플리케이션 플랫폼입니다.

이러한 Red Hat OpenShift 기반의 Red Hat Middleware는 모든 환경과 애플리케이션 라이프사이클 전반에 걸쳐 클라우드 네이티브 애플리케이션을
배포, 제공, 확장할 수 있도록 일관되고 통합된 환경을 제공합니다. 

7) Microservices with OpenShift

```

## Credit

- [Application Development using Microservices and Serverless](https://www.coursera.org/learn/applications-development-microservices-serverless-openshift)
- [Certification-Link]
