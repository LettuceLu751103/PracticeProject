<template>
    <h3>{{ title }}</h3>
    <p>當前點擊次數 : {{ count }}</p>
    <button v-on:click="counting">點擊+1</button>
    <p>當前的 title : {{ message }}</p>
    <p>傳遞的參數 : {{ msg }}</p>
    <button v-on:click="getTitle('我點擊了獲得title按鈕')">點擊獲得 title</button>
    <div>
        <!-- 注意 @click.prevent 後面加的 prevent , 可以阻止事件 -->
        <a href="https://www.google.com.tw" @click.prevent="clickHandle">Google 不跳轉</a>
    </div>
    <div>
        
        <a href="https://www.google.com.tw">跳轉 Google</a>
    </div>
    
</template>

<script>
    export default {
        data(){
            return {
                title:'事件處理',
                count: 0,
                message:'',
                msg:''
            }
        },
        methods:{
            counting(e){
                console.log(e.target)
                console.log(e.target.innerHTML)
                console.log('按鈕被點擊了')
                this.count++
            },
            getTitle(msgParameter){
                this.message = this.title
                this.msg = msgParameter
            },
            clickHandle(e){
                console.log('點擊但是不跳轉Google')
            }
        }
    }
</script>