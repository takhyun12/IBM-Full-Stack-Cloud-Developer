# Developing Cloud Apps with Node.js and React

Certificate of the course that is offered at Coursera and IBM.

#### Author: Tackhyun Jung

#### Status: Completed

This repository is created to keep track of [Developing Cloud Apps with Node.js and React](https://www.coursera.org/learn/node-js) provided by Coursera.
This educational program is developed by IBM and designed to teach how to program in cloud computing environment.

## Learning Objectives

- Introduction to Server-Side JavaScript `week 1`
- Asynchronous I/O with Callback Programming `week 2`
- Express Web Application Framework `week 3`
- Building a Rich Front-End Application using REACT & ES6 `week 4`
- Final Assignment `week 5`

## Assignment
I developed a new site that uses IBM Watson services to find sentiments and emotions in text. The application was built using Express.js in the back-end and React.js in the front-end application.

![1](https://user-images.githubusercontent.com/41291493/111033848-7d597280-8456-11eb-9406-5ebbc46cc933.png)

![2](https://user-images.githubusercontent.com/41291493/111033849-7e8a9f80-8456-11eb-8422-8a4c761296e2.png)

## Note

```
1) Node.js
Node.js는 확장성 있는 네트워크 애플리케이션(특히 서버 사이드) 개발에 사용되는 소프트웨어 플랫폼이다
작성 언어로 자바스크립트를 활용하며 Non-blocking I/O와 단일 스레드 이벤트 루프를 통한 높은 처리 성능을 가지고 있다

Node.JS는 웹브라우저에 종속적인 자바스크립트에서 외부에서 실행할 수 있는 Runtime 환경인 자바스크립트 엔진 (V8 Engine)을 활용한다

2) Javascript의 호출스택과 이벤트 루프

function first() {
   second()
   console.log('첫 번째 실행')
}
function second() {
   third()
   console.log('두 번째 실행')
}
function third() {
   console.log('세 번째 실행')
}
first()

위 코드를 기준으로 호출 스택의 자료 구조로 first(), second(), third()가 메모리에 입력될 때, 
스택 특징 Last In First Out(후입선출)에 따라 세 번째, 두 번째, 첫 번째 순서로 실행된다

3) Node.js의 특징
Node.js는 이벤트 루프와 함께 단일 쓰레드 모델을 사용합니다
이벤트 메커니즘은 서버가 멈추지않고 반응하도록 해주어 서버의 확장성을 키워줍니다
반면, 일반적인 웹서버는(Apache) 요청을 처리하기 위하여 제한된 쓰레드를 생성합니다
이러한 특징에 따라 Node.js는 쓰레드를 한개만 사용하고 Apache 같은 웹서버보다 훨씬 많은 요청을 처리할 수 있습니다.

Node.js 라이브러리의 모든 API는 비동기식입니다, 멈추지 않는다는거죠 (Non-blocking) 
Node.js 기반 서버는 API가 실행되었을때, 데이터를 반환할때까지 기다리지 않고 다음 API 를 실행합니다
그리고 이전에 실행했던 API가 결과값을 반환할 시, NodeJS의 이벤트 알림 메커니즘을 통해 결과값을 받아옵니다

구글 크롬의 V8 자바스크립트 엔진을 사용하여 빠른 코드 실행을 제공합니다

CPU 사용률이 높은 어플리케이션에선 Node.js 사용을 권장하지 않습니다

4) React
웹 개발을 하게 될 때, 귀찮은 DOM 관리와 상태값 업데이트 관리를 최소화하고, 오직 기능 개발, 
그리고 사용자 인터페이스를 구현하는 것에 집중 할 수 있도록 하기 위해서,
대표적으로 React, Angular, Ember, Backbone, Vue 등의 프론트엔드 프레임워크들이 만들어졌다

React는 “컴포넌트” 라는 개념에 집중이 되어있는 라이브러리이다
컴포넌트는 데이터를 넣으면 우리가 지정한 유저 인터페이스를 조립해서 보여줍니다

브라우저에게 DOM 기반으로 작동하는 페이지는 지속적으로 새로 뷰를 만들어버리라고 하면 성능적으로 엄청난 문제가 발생하게 됩니다
따라서,Virtual DOM이라는 개념을 사용하게 되는데 데이터가 바뀌었을 때 더 이상 어떻게 업데이트 할 지를 고려하는게 아니라, 
그냥 일단 바뀐 데이터로 일단 그려놓고 비교를 한다음에, 바뀐 부분만 찾아서 바꿔주는 원리이다

즉, DOM의 변화를 최소화하여 성능적으로 최적화를 수행하는 개념이다
```

## Credit

- [Developing Cloud Apps with Node.js and React](https://www.coursera.org/learn/node-js)
- [Certification-Link](https://www.coursera.org/account/accomplishments/verify/ARUZJ5MFXRY7)
