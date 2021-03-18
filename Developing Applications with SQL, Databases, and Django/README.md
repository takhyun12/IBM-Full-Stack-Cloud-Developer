# Developing Applications with SQL, Databases, and Django

Certificate of the course that is offered at Coursera and IBM.

#### Author: Tackhyun Jung

#### Status: Completed

This repository is created to keep track of [Developing Applications with SQL, Databases, and Django](https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django?) provided by Coursera.
This educational program is developed by IBM and designed to teach how to program in cloud computing environment.

![Certificate](https://user-images.githubusercontent.com/41291493/111605183-6f6e6d80-8819-11eb-930c-0b25389b425a.png)

## Learning Objectives

- Getting Started with SQL & Relational Databases `week 1`
- ORM: Bridging the Gap Between the Real World and Relational Model `week 2`
- Full-stack Django Development `week 3`
- Consolidate and Deploy Your Django App `week 4`
- Final Project: Enhance Online Course App with New Features `week 5`

## Assignment

I did my Django full-stack skills to design and implement models, templates, and views. 

![onlinecourse_app_er](https://user-images.githubusercontent.com/41291493/111605193-709f9a80-8819-11eb-9f91-35211c0b26e8.png)


## Note

```
1) Relational Databases : 키(key)와 값(value)들의 간단한 관계를 테이블화 시킨 매우 간단한 원칙의 정보 저장소
관계형 모델 : 데이터를 컬럼(column)과 로우(row)를 이루는 하나 이상의 테이블(또는 관계)로 정리하며, 고유 키(Primary key)가 각 로우를 식별한다.
키 (Key) : 테이블의 각 로우에는 각각의 고유 키(key)가 있다. 한 테이블 안의 로우는 다른 테이블들 로우의 고유 키를 위한 컬럼을 추가함으로써 매핑이 가능하다.
관계 (Relationships) : 관계는 테이블 간에 둘 다 존재한다. 이 관계들은 일대일, 일대다, 다대다, 이렇게 세 가지 형태로 이루어진다.
트랜잭션(Transaction) : 데이터베이스의 상태를 변환시키는 하나의 논리적 기능을 수행하기 위한 작업의 단위 또는 한꺼번에 모두 수행되어야 할 일련의 연산을 의미한다.

2) NoSQL(Not Only SQL)
인터넷이 활성화되고, 소셜네트워크 서비스 등이 등장하면서 관계형 데이터 또는 정형데이터가 아닌 데이터, 
즉 비정형데이터를 보다 쉽게 담아서 저장하고 처리할 수 있는 구조를 가진 데이터 베이스들이 관심을 받게 되어 NoSQL이 각광받고 있다.

NoSQL의 특징
- 관계형 모델을 사용하지 않으며 테이블간의 조인 기능 없음
- 직접 프로그래밍을 하는 등의 비SQL 인터페이스를 통한 데이터 액세스
- 대부분 여러 대의 데이터베이스 서버를 묶어서(클러스터링) 하나의 데이터베이스를 구성
- 관계형 데이터베이스에서는 지원하는 Data처리 완결성(Transaction ACID 지원) 미보장
- 데이터의 스키마와 속성들을 다양하게 수용 및 동적 정의 (Schema-less)
- 데이터베이스의 중단 없는 서비스와 자동 복구 기능지원
- 다수가 Open Source로 제공
- 확장성, 가용성, 높은 성능

NoSQL의 종류
- Key Value DB : Key와 Value의 쌍으로 데이터가 저장되는 가장 단순한 형태의 모델. 예) Riak, Vodemort, Tokyo
- Wide Columnar Store : Key Value 에서 발전된 형태의 Column Family 데이터 모델. 예) HBase, Cassandra, ScyllaDB
- Document DB : JSON, XML과 같은 Collection 데이터 모델. 예) MongoDB, CoughDB
- Graph DB : Nodes, Relationship, Key-Value 데이터 모델. 예) Neo4J, OreientDB

3) Object-Relational Mapping (ORM) : 객체와 관계형 데이터베이스의 데이터를 자동으로 매핑(연결)해주는 것을 말한다.
객체 지향 프로그래밍은 클래스를 사용하고, 관계형 데이터베이스는 테이블을 사용한다.

ORM의 장점
선언문, 할당, 종료 같은 부수적인 코드가 없거나 급격히 줄어든다.
재사용 및 유지보수의 편리성이 증가한다.

ORM의 단점
프로젝트의 복잡성이 커질경우 난이도 또한 올라갈 수 있다.
잘못 구현된 경우에 속도 저하 및 심각할 경우 일관성이 무너지는 문제점이 생길 수 있다.

4) Django
장고(Django)는 파이썬으로 작성된 오픈 소스 웹 프레임워크로, 모델-뷰-컨트롤러(MVC) 패턴을 따르는 개발 프레임워크이다.
고도의 데이터베이스 기반 웹사이트를 작성하는 데 있어서 수고를 더는 것이 장고의 주된 목표이다.
컴포넌트의 재사용성(reusability)과 플러그인화 가능성(pluggability), 빠른 개발 등이 주된 특징이다.

5) Django Model-View-Template Pattern
장고는 파이썬으로 코딩한 모델을 관계형 데이터베이스로 구축해주는 모델(Model), HTTP 요청을 처리하는 웹 템플릿 시스템인 뷰(View), 
URL의 라우팅을 처리하는 URL 컨트롤러 (Controller)로 구성된 MVC 디자인 패턴을 따른다.

하지만 전통적인 MVC 디자인 패턴에서 이야기하는 컨트롤러의 기능을 프레임워크를 자체에서 하기 때문에,
모델(Model), 템플릿(Template), 뷰(View)로 분류해 MTV 이라고 부른다.

6) CRUD
CRUD는 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능인 Create(생성), Read(읽기), Update(갱신), Delete(삭제)를 묶어서 일컫는 말이다. 

7) Bootstrap
부트스트랩(Bootstrap)은 웹사이트를 쉽게 만들 수 있게 도와주는 HTML, CSS, JS 프레임워크이다. 
하나의 CSS로 휴대폰, 태블릿, 데스크탑까지 다양한 기기에서 작동한다. 다양한 기능을 제공하여 사용자가 쉽게 웹사이트를 제작, 유지, 보수할 수 있도록 도와준다.
```

## Credit

- [Developing Applications with SQL, Databases, and Django](https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django?)
- [Certification-Link](https://www.coursera.org/account/accomplishments/verify/EBC7FMWLP775)
