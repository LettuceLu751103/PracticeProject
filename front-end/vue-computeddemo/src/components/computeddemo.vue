<template>
    <h3>計算屬性</h3>
    <p> {{ name }} </p>
    <p> 廠牌 : {{ result.brand }}</p>
    <p v-for="(item, index) in content" :key="index">技術 : {{ item }}</p>
    <p>技術有幾門(計算屬性) : {{ countlength }}</p>
    <p>技術有幾門(函數方法) : {{ countLengthByMethods() }}</p>
    <p>可以注意到在表達是當中像這樣調用一個函數也會獲得和計算屬性相同的結果.</p>
    <h3>重點區別</h3>
    <p>計算屬性: 會基於其響應式依賴被緩存. 一個計算屬性僅會在其響應式更新時才重新計算</p>
    <p>方法: 方法調用總是會在重新渲染時候再次執行函數</p>
</template>

<script>
    export default {
        data(){
            return {
                name: 'Lettuce Lu',
                content: ['前端', 'Java', 'Python'],
                result: {
                    brand: 'Cisco'
                }
            }
        },
        // 計算屬性
        computed: {
            countlength(){
                return this.content.length > 0 ? '技術超過一門' : '沒有半門技術'
            }
        },
        // 函數方法
        methods: {
            countLengthByMethods(){
                return this.content.length > 0 ? 'YES' : 'NO'
            }
        }
    }
</script>