<template>
    <div class="footer">
        <H3>Footer</H3>
        <p>從 APP.vue 父組件傳送過來的字符串 : <span class="color">{{ message_footer }}</span></p>
        <p v-for="name in names">從 APP.vue 父組件傳送過來的陣列 : <span class="color">{{ name }}</span></p>
        <div v-for="obj in objresult" class="footerdata">
            <p>id: {{ obj._id }}</p>
            <p>年度 : {{ obj.年度 }}</p>
            <p>社區戶數 : {{ obj.社區戶數 }}</p>
            <p>社區人口數 : {{ obj.社區人口數 }}</p>
        </div>
    </div>
    
</template>

<script>
export default {
    data(){
        return {

        }
    },
    props:["message_footer", 'names', 'objresult']
}
</script>

<style scoped>
.footer {
    width: 100%;
    box-sizing: border-box;
    border: 5px solid grey;
    text-align: start;
    float: left;
    margin-top: 20px;
}
.color {
    color: red;
}
.footerdata {
    text-align: start;
}
</style>