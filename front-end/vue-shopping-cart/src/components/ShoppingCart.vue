<template>
    <h3>ShoppingCart Demo</h3>
    <p>歡迎 {{ myComputedName }} 回來!!!</p>
    <p>原始資料屬性 : {{ myName }}</p>
    <p>計算屬性產生結果 : {{ myComputedName }}</p>
    <div>
        <ul>
            <li>
                <div>
                    <input type="checkbox" v-model="isAllChecked" @change="allChangeHandler()"> 全選/全不選
                </div>
            </li>
            <template>
                
            </template>
            <li v-for="(result, index) in results" :key="result.id">
                <div>
                    <input type="checkbox" :name="result.title" :id="result.id" v-model="checkList" :value="result" @change="itemChangeHandler()">
                </div>
                <img :src="result.poster" alt="">
                <div>
                    <p>{{ result.title }}</p>
                    <p style="color: red;">價格 : {{ result.price }}</p>
                </div>
                <div>
                    <button @click="result.number--" :disabled="result.number===1"> - </button>
                    <input type="text" :value="result.number" style="text-align: center;">
                    <button @click="result.number++" :disabled="result.number === result.limit"> + </button>
                </div>
                <div>
                    <button @click="deleteHandler(index, result.id)">Delete</button>
                </div>
            </li>
            <li>
                <div>
                    總金額 : {{ sum() }}
                </div>
            </li>
            {{ checkList }}
        </ul>
        
        
        
        
        
    </div>
</template>

<script>
export default {
    data(){
        return {
            myName: 'ethan',
            isAllChecked: false,
            checkList: [], // 勾選的商品列表
            results: [
                {
                    id: 1,
                    title: '把生活過成賞心悅目的好日子',
                    price: 250,
                    number: 1,
                    poster: 'https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/101/16/0011011609.jpg&v=678f8551k&w=270&h=270',
                    limit: 2
                },
                {
                    id: 2,
                    title: '有錢人的書櫃總有一本心理學書',
                    price: 250,
                    number: 1,
                    poster: 'https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/098/25/0010982531.jpg&v=65cde7aak&w=270&h=270',
                    limit: 5
                },
                {
                    id: 3,
                    title: '人氣爆棚高情商養成術：好好說話+好好溝通+好好交朋友',
                    price: 752,
                    number: 1,
                    poster: 'https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/101/27/0011012765.jpg&v=678e962ak&w=270&h=270',
                    limit: 6
                },
                {
                    id: 4,
                    title: '廣重TOKYO　名所江戶百景',
                    price: 363,
                    number: 1,
                    poster: 'https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/079/71/0010797102.jpg&v=5b83e0bck&w=270&h=270',
                    limit: 5
                },
                {
                    id: 5,
                    title: '你的問題不是問題：轉化困境為力量的薩提爾對話模式',
                    price: 264,
                    number: 1,
                    poster: 'https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/101/62/0011016296.jpg&v=67c9796dk&w=270&h=270',
                    limit: 9
                },
            ]
        }
    },
    methods: {
        sum(){
            let total = 0
            for(let i=0; i<this.checkList.length; i++){
                total += this.checkList[i].number * this.checkList[i].price
            }
            return total
        },
        deleteHandler(index, id){
            console.log(index, id)
            this.results.splice(index,1)
            // 同步更新 checkList
            this.checkList = this.checkList.filter(item=>item.id !== id)
            this.itemChangeHandler()
            
        },
        allChangeHandler(){
            this.checkList = this.isAllChecked ? this.results : []
        },
        itemChangeHandler(){
            if(this.results.length === 0){
                this.isAllChecked = false
                return 
            }
            this.isAllChecked = this.checkList.length === this.results.length
            
        }
    },
    computed: {
        myComputedName(){
            this.myName = this.myName.substring(0, 1).toUpperCase() + this.myName.substring(1)
            return this.myName
        }
    }
}
</script>

<style>
li {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border: 2px solid grey;
    box-sizing: border-box;
    margin-top: 5px;
}

li img {
    width: 200px;
}
</style>