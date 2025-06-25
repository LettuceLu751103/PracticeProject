
<template>
    <h3>{{ title }}</h3>
    <div>
        <p v-for="name in members"> 組員名稱 : {{ name }}</p>
    </div>
    <div>
        <ul>
            <li v-for="device in deviceList">IP: {{ device.ip }}, brand: {{ device.brand }}, model: {{ device.model }}</li>
        </ul>
    </div>
    <div>
        <h4>Key 屬性添加到 v-for 當中</h4>
        <p v-for="(number, index) in numbers" :key='index'>當前索引 {{ index }} - {{ number }}</p>
    </div>
    
</template>

<script>
    export default {
        data(){
            return {
                title: '列表渲染',
                members: ['Brian', 'Ruby', 'Helen', 'Horace', 'Jack'],
                deviceList: [
                    { ip:'192.168.10.15', brand:'Cisco', model:'ASR1002-HX'},
                    { ip:'10.255.230.77', brand:'Juniper', model:'SRX-345'},
                    { ip:'172.16.55.30', brand:'Cisco', model:'C93180-EX'}
                ],
                numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            }
        }
    }
</script>