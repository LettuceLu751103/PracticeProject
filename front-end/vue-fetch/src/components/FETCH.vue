<template>
    <h3>{{ title }}</h3>
    <button @click="readDataHandler()">獲取資料</button>
    <ul v-for="data in dataList">
        <li>{{ data.id }}</li>
        <li>{{ data.name }}</li>
        <li>{{ data.age }}</li>
    </ul>
    <button @click="writeDataHandler()">寫入資料</button>
    <div class="container">
        <div class="item left">1</div>
        <div class="item left">2</div>
        <div class="item left">3</div>
        <div class="item left">4</div>
        <div class="item right">5</div>
        <div class="item right">6</div>
        <div class="item right">5</div>
        <div class="item right">6</div>
        <div class="item right">5</div>
        <div class="item right">6</div>
        <div class="item right">5</div>
        <div class="item right">6</div>
        <div class="item right">5</div>
        <div class="item right">6</div>
    </div>
    <div class="page-container">
        <div class="page-item active"><a href="">1</a></div>
        <div class="page-item"><a href="">2</a></div>
        <div class="page-item"><a href="">3</a></div>
        <div class="page-item"><a href="">4</a></div>
        <div class="page-item"><a href="">5</a></div>
        <div class="page-item"><a href="">6</a></div>
        <div class="page-item"><a href="">7</a></div>
        <div class="page-item"><a href="">8</a></div>
        <div class="page-item"><a href="">9</a></div>
        <div class="page-item"><a href="">10</a></div>
        <div class="page-item"><a href="">下一頁</a></div>
    </div>
</template>

<style scoped>
.page-container {
    width: 1200px;
    height: 60px;
    margin: 10 auto;
    border: 1px solid black;
    border-radius: 5px;
}
.page-item {
    margin:10px;
    width:60px;
    height: 40px;
    line-height: 40px;
    text-align:center;
    border: 1px solid grey;
    display: inline-block;
    border-radius: 5px;
}
a {
    text-decoration: none;
}
.page-item:hover {
    background-color: #2894FF;
    color: white;
}
.active {
    background-color: #2894FF;
    color: white;
}

.container {
    width: 1080px;
    height: 200px;
    margin: 0 auto;
    background-color: grey;
}
.item {
    width: 100px;
    background-color: yellow;
    margin-left: 5px;
    margin-top: 10px;
    float: left;
    text-align: center;
    border: 1px solid black;
    box-sizing: border-box;
}
.left {
    height: 170px;
}
.right {
    height: 80px;
}
</style>

<script>
export default {
    data(){
        return {
            title: 'Axios Demo',
            dataList: []
        }
    },
    methods: {
        readDataHandler(){
            axios.get("http://localhost:3000/userdata")
            .then(res => {
                console.log(res)
                this.dataList = res.data
                return this.dataList
            })
        },
        writeDataHandler(){
            // axios.get("http://localhost:3000/userdata")
            //     .then(res => {
            //         console.log(res.data)
            //         this.dataList = res.data
            //         return this.dataList
            //     })

            axios.post("http://localhost:3000/userdata",{
                name: "banana",
                age: 22
            })
            .then(res => {
                console.log(res)
            })
            .catch(err => {
                console.log(err)
            })
                
        }
    }
}
</script>