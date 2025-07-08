
<template>
    <div>
        <h3  class="article">Article</h3>
        <div>
        <p>{{ message }}</p>
        <p v-for="name in names">{{ name }}</p>
        </div>
    </div>
</template>


<script>
export default {
    data(){
        return {

        }
    },
    props: ["message", 'names']
}
</script>


<style scoped>
.article {
    width: 80%;
    margin: 0 auto;
    text-align: center;
    line-height: 100px;
    box-sizing: border-box;
    border: 5px solid red;
    margin-top: 50px;
    background: #999;
}


</style>