
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
        <p v-for="(member, index) in members" key="index">當前索引 {{ key }} - {{ member }}</p>
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
                ]
            }
        }
    }
</script>