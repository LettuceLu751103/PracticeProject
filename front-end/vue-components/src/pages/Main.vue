<template>
    <div class="main">
        <h3>Main</h3>
        <Article :message="message"></Article>
        <Article :names="names"></Article>
    </div>
    
</template>

<script>
import Article from './Article.vue'
export default {
    data(){
        return {
            message: '這是從Main組件傳遞過來的訊息',
            names: ['Joy', 'Lettuce', 'Andrew', 'Brian']
        }
    },
    components: {
        Article
    }
}
</script>

<style scoped>
.main {
    float: left;
    width: 70%;
    height: 600px;
    border: 5px solid #999;
    box-sizing: border-box;

}
</style>