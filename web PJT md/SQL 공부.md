# SQL 공부





### REGEXP



- 글자 시작이 (a, e, i, o, u) 인 city를 출력(중복 x)

```
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[aeiou]';
```



- 글자의 마지막이(a, e, i, o, u)인 city를 출력(중복 x)

```
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '[aeiou]$';
```



- 글자의 시작과 끝이 (a, e, i, o, u)인 city를 출력(중복 x)

```
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[aeiou]' AND CITY REGEXP '[aeiou]$';
```



- 글자의 시작이 (a, ,e, i, o, u)가 아닌 city를 출력(중복 x)

```
SELECT DISTINCT CITY FROM STATION WHERE CITY NOT REGEXP '^[aeiou]';
```



- 글자의 마지막이(a, e, i, o, u)가 아닌 city를 출력(중복 x)

```
SELECT DISTINCT CITY FROM STATION WHERE CITY NOT REGEXP '[aeiou]$';
```



- ** either do not start with vowels or do not end with vowels

```
SELECT DISTINCT CITY 
    FROM STATION 
    WHERE CITY REGEXP '^[^aeiou]' 
    OR CITY REGEXP '[^aeiou]$'; 
```



- CITY의 시작과 마지막이 (a, e, i, o, u)가 아닌 city를 출력(중복 x)

```
SELECT DISTINCT CITY FROM STATION WHERE CITY NOT REGEXP '^[aeiou]' AND CITY NOT REGEXP '[aeiou]$';
```





...ING