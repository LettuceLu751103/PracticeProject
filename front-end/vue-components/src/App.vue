
<template>
  <Header></Header>
  <Main></Main>
  <Aside></Aside>
  <Footer :message_footer="message_footer" :names="names" :objresult="objresult"></Footer>
</template>

<script>
import Header from './pages/Header.vue'
import Main from './pages/Main.vue'
import Aside from './pages/Aside.vue'
import Footer from './pages/Footer.vue'

export default {
  data(){
    return {
      message_footer: '傳給 footer 的訊息',
      names: ['Brian', 'Helen', 'Horace', 'Jack', 'Ethan'],
      objresult: [
        {
        "_id": 1,
        "_importdate": {
        "date": "2025-06-26 11:58:46.927191",
        "timezone_type": 3,
        "timezone": "Asia/Taipei"
        },
        "年度": " 104年",
        "社區發展協會總數": "361",
        "社區戶數": "1043948",
        "社區人口數": "2704810",
        "理監事人數": "5662",
        "參加社區發展協會會員數": "25292",
        "實際使用總經費": "17757875"
        },
        {
        "_id": 2,
        "_importdate": {
        "date": "2025-06-26 11:58:46.980725",
        "timezone_type": 3,
        "timezone": "Asia/Taipei"
        },
        "年度": " 105年",
        "社區發展協會總數": "354",
        "社區戶數": "1047284",
        "社區人口數": "2695704",
        "理監事人數": "5494",
        "參加社區發展協會會員數": "25095",
        "實際使用總經費": "21900413"
        },
        {
        "_id": 3,
        "_importdate": {
        "date": "2025-06-26 11:58:46.982441",
        "timezone_type": 3,
        "timezone": "Asia/Taipei"
        },
        "年度": " 106年",
        "社區發展協會總數": "362",
        "社區戶數": "1050755",
        "社區人口數": "2683257",
        "理監事人數": "5631",
        "參加社區發展協會會員數": "25042",
        "實際使用總經費": "27503082"
        },
        {
        "_id": 4,
        "_importdate": {
        "date": "2025-06-26 11:58:46.983864",
        "timezone_type": 3,
        "timezone": "Asia/Taipei"
        },
        "年度": " 107年",
        "社區發展協會總數": "360",
        "社區戶數": "1056233",
        "社區人口數": "2668572",
        "理監事人數": "5849",
        "參加社區發展協會會員數": "23451",
        "實際使用總經費": "26241929"
        },
        {
        "_id": 5,
        "_importdate": {
        "date": "2025-06-26 11:58:46.985269",
        "timezone_type": 3,
        "timezone": "Asia/Taipei"
        },
        "年度": " 108年",
        "社區發展協會總數": "375",
        "社區戶數": "1060880",
        "社區人口數": "2645041",
        "理監事人數": "5639",
        "參加社區發展協會會員數": "24468",
        "實際使用總經費": "25523893"
        }
      ],
    }
  },
  // 注入組件
  components:{
    Header,
    Main,
    Aside,
    Footer
  }
}
</script>

<style>
.color {
    color:red;
    font-size: 20px;
}
</style>