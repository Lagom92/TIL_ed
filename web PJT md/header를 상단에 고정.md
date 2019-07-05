# 반응형 웹 페이지 제작



### 1-3. 스크롤시 헤더가 같이 움직이도록 구현



- MainHeader.vue

```
</script>
<style scoped>
.head {
  position:fixed;
  left:0;
  top:0;
  width:100vw;
  z-index:200;
  height: 60px;
  text-align: left;
}

</style>
```

