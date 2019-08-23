# SQL

SQL 전문가 가이드 2010 Edition을 공부한 내용을 정리했다.



### SQL(Structured Query Language)

데이터베이스를 직접적으로 액세스 할 수 있는 언어

데이터를 정의(Data Definition)하고, 조작(Data Manipulation)하며, 조작한 결과를 적용하거나 취소할 수 있고(Transaction Control), 접근 권한을 제어(Data Control) 처리들로 구성된다.



# 과목 1. 데이터 모델링의 이해

## 제 1 절 데이터 모델의 이해

1. 모델링의 이해

   1. 모델링의 정의

      - 모델을 만들어 가는 일
      - 복잡한 '현실세계'를 단순화시켜 표현하는 것
      - 모델이란 사물 또는 사건에 관한 양상(Aspect)이나 관점(Perspective)을 연관된 사람이나 그룹을 위하여 명확하게 하는 것

      

   2. 모델링의 특징

      - 추상화, 단순화, 명확화

      1. 추상화

         다양한 현상을 일정한 양식인 표기법에 의해 표현한다는 것

      2. 단순화

         복잡한 현실세계를 약속된 규약에 의해 제한된 표기법이나 언어로 표현하여 쉽게 이해할 수 있도록 하는 개념

      3. 명확화

         누구나 이해하기 쉽게 하기 위해 대상에 대한 애매모호함을 제거하고 정확하게 현상을 기술하는 것

      즉, 모델링은 현실세계를 추상화, 단순화, 명확화 하기 위해 일정한 표기법에 의해 표현하는 기법이라고 할 수 있다.

      

   3. 모델링의 세 가지 관점

      - 데이터 관점, 프로세스 관점, 데이터와 프로셋의 상관관점

      1. 데이터 관점

         업무가 어떤 데이터와 관련이 있는지 또는 데이터간의 관계는 무엇인지에 대해서 모델링하는 방법(What, Data)

      2. 프로세스 관점

         - 업무가 실제하고 있는 일은 무엇인지 또는 무엇을 해야 하는지를 모델링 하는 방법(How, Process)

      3. 데이터와 프로세스의 상관관점

         - 업무가 처리하는 일의 방법에 따라 데이터는 어떻게 영향을 받고 있는지 모델링하는 방법(Interaction)

         

2. 데이터 모델의 기본 개념의 이해

   1. 데이터 모델링의 정의

      - 정보시스템을 구축하기 위해 해당 업무에 어떤 데이터가 존재하는지 또는 업무가 필요로 하는 정보는 무엇인지를 분석하는 방법
      - 기업 업무에 대한 종합적인 이해를 바탕으로 데이터에 존재하는 업무 규칙(Business Rule)에 대하여 참 또는 거짓을 판별할 수 있는 사실(사실명제)을 데이터에 접근하는 방법(How), 사람(Who), 전산화와는 별개의(독립적인)관점에서 이를 명확하게 표현하는 추상화 기법

   2. 데이터 모델링을 하는 주요한 이유

      1. 업무정보를 구성하는 기초가 되는 정보들을 일정한 표기법에 의해 표현함으로써 정보시스템 구축의 대상이 되는 업무 내용을 정확하게 분석하는 것
      2. 분석된 모델을 가지고 실제 데이터베이스를 생성하여 개발 및 데이터관리에 사용하기 위한 것

      >데이터 모델링이란..
>
      >정보시스템을 구축하기 위한 데이터관점의 업무 분석 기법
>
      >현실세계의 데이터(What)에 대해 약속된 표기법에 의해 표현하는 과정
>
      >데이터베이스를 구축하기 위한 분석/설계의 과정
      
      
      
   3. 데이터 모델이 제공하는 기능
   
      - 시스템을 현재 또는 원하는 모습으로 가시화하도록 도와준다.
   - 시스템의 구조와 행동을 명세화 할 수 있게 한다.
      - 시스템을 구축하는 구조화된 틀을 제공한다.
   - 시스템을 구축하는 과정에서 결정한 것을 문서화한다.
      - 다양한 영역에 집중하기 위해 다른 영역의 세부 사항은 숨기는 다양한 관점을 제공한다.
   - 특정 목표에 따라 구체화된 상세 수준의 표현방법을 제공한다.
   
      
   
3. 데이터 모델링의 중요성 및 유의점

   데이터 모델링이 중요한 이유: 파급효과, 복잡한 정보 요구사항의 간결한 표현, 데이터 품질

   

   1. 파급효과(Leverage)

      시스템이 구축되어 가면서 많은 단위테스트를 하고 병행테스트, 통합테스트를 수행 하게 된다. 이러한 과정 중에서 데이터 모델의 변경이 불가피한 상황이 발생한다면 데이터 구조의 변경에 따른 표준 영향 분석, 응용 변경 영향 분석 등 많은 영향 분석이 일어난다. 그 이후에 해당 분야의 실제적인 변경 작업이 발생하게 된다. 즉, 데이터 구조의 변경으로 인한 일련의 변경작업은 전체 시스템 구축  프로젝트에서 큰 위험요소가 된다. 그래서  데이터 설계가 중요하다.

   2. 복잡한 정보 요구사항의 간결한 표현(Conciseness)

      데이터 모델은 구축할 시스템의 정보 요구사항과 한계를 가장 명확하고 간결하게 표현할 수 있는 도구이다. 정보 요구사항을 파악하는 좋은 방법은 데이터 모델을 리뷰하면서 파악하는 것 이다. 데이터 모델은 시스템을 구축하는 많은 관련자들이 설계자의 생각대로 정보요구사항을 이해하고 이를 운용할 수 있는 애플리케이션을 개발하고 데이터 정합성을 유지할 수 있도록 하는 것이다. 모델이 갖추어야 할 가장 중요한 점은 정보 요구사항이 정확하고 간결하게 표현되어야 한다는 것이다.

   3. 데이터 품질(Ddata Quality)

      데이터 품질의 문제는 초기에는 인지를 못하다가 시간이 지나고 데이터의 양이 많아 지면서 이를 사용하려고 할때 문제가 될 수 있다. 중복 데이터의 미정의, 데이터 구조의 비즈니스 정의의 불충분, 동일한 성격의 데이터를 통합하지 않고 분리함으로써의 나타나는 데이터 불일치 등의 데이터 구조의 문제로 인한 데이터 품질 문제는 발생 하지 않도록 해야 한다.

      

      - 데이터 모델링을 할 때 유의점

        1. 중복(Duplication)

           데이터 모델은 같은 데이터를 사용하는 사람, 시간, 그리고 장소를 파악하는데 도움을 준다. 이러한 지식 응용은 데이터가 여러 장소에 같은 정보를 저장하는 잘못을 하지 않도록 한다. 

        2. 비유연성(Inflexbility)

           데이터 모들을 어떻게 설계했느냐에 따라 사소한 업무변화에도 데이터 모델이 수시로 변경됨으로써 유지보수의 어려움을 가중시킬 수 있다. 데이터의 정의를 데이터의 사용 프로세스와 분리함으로써 데이터 모델링은 데이터 혹은 프로세스의 작은 변화가 애플리케이션과 데이터베이스에 중대한 변화를 일으킬 수 있는 가능성을 줄인다.

        3. 비일관성(Inconsistency)

           데이터의 중복이 없더라도 비일관성은 발생한다. 개발자가 다른 데이터와 모순된다는 고려 없이 일련의 데이터를 수정 할 수 있기 때문이다. 데이터 모델링을 할 때 데이터와 데이터간 상호 연관 관계에 대한 명확한 정의는 이러한 위험을 사전에 예방 할 수 있도록 해준다.

   4. 데이터 모델링의 3단계 진행

      데이터베이스가 만들어지는 과정은 추상화 수준에 따라 개념적 데이터 모델, 논리적 데이터 모델, 물리적 데이터 모델로 정리 할 수 있다.
      
      
      
      개념 - 논리 - 물리 데이터 모델
      
      | 데이터 모델링        | 내용                                                         |
      | -------------------- | ------------------------------------------------------------ |
      | 개념적 데이터 모델링 | 추상화 수준이 높고 업무중심적이고 포괄적인 수준의 모델링 진행, 전사적 데이터 모델링, EA수립시 많이 이용 |
      | 논리적 데이터 모델링 | 시스템으로 구축하고자 하는 업무에 대해 Key, 속성, 관계 등을 정확하게 표현, 재사용성이 높음 |
      | 물리적 데이터 모델링 | 실제로 데이터베이스에 이식할 수 있도록 성능, 저장 등 물리적인 성격을 고려하여 설계 |
      
      개념적 데이터 모델링이 가장 추상적이고 물리적 데이터 모델링이 가장 구체적이다.
      
      1. 개념적 데이터 모델링(Conceptual Data Modeling)
      
         - 개념적 데이터베이스 설계(개념 데이터 모델링)는 조직, 사용자의 데이터 요구사항을 찾고 분석하는데서 시작한다.
         - 어떤 자료가 중요하고 어떤 자료가 유지되어야 하는지 결정하는것도 포함된다.
         - 핵심 엔티티와 그들 간의 관계를 발견하고 엔티티-관계 다이어그램을 생성 한다.
         - 엔티티-관계 다이어그램은 조직과 다양한 데이터베이스 사용자에게 어떠한 데이터가 중요한지 나타내기 위해서 사용된다.
         - 데이터 모델링 과정이 전 조직에 걸쳐 일루어진다면 그것은 전사적 데이터 모델(Enterprise Data Model)이라고 불린다.
         - 조직의 데이터 요구를 공식화 하는것의 기능
           1. 개념 데이터 모델은 사용자와 시스템 개발자가 데이터 요구 사항을 발견하는 것을 지원한다.
           2. 개념 데이터 모델은 현 시스템이 어떻게 변형되어야 하는가를 이해하는데 유용하다.
      
      2. 논리적 데이터 모델링(Logical Data Modeling)
      
         - 데이터베이스 설계 프로세스의 Input으로써 비즈니스 정보의 논리적인 구조와 규칙을 명확하게 표현하는 기법 또는 과정
      
         - 누가(Who), 어떻게(How: Process) 그리고 전산화와는 별개로 비즈니스 데이터에 존재하는 사실들을 인식하여 기록하는 것
      
         - 데이터 모델링 과정에서 가장 핵심이 되는 부분이 논리 데이터 모델링이라고 할 수 있다.
      
           ///이어서 20 page



​				