<template>
    <div>
        <nav>
            <Toolbar :pt="{
                root: {
                    style: {
                        'border-radius': '0px',
                    }
                }
            }">
                <template #start>
                    <Sidebar />
                    <h4 class="m-2">Teacher Specifications</h4>
                </template>
                <template #end>
                    <SplitButton label="Hi! renz@gmail.com" :model="items" icon="pi pi-plus" raised severity="contrast" size="small" :pt="{
                        ptMenu: {
                            style: {
                                'text-decoration': 'none',
                                'color': 'black',
                            }
                        }
                    }"></SplitButton>
                    <!-- <Button label="About" @click="router.push({name: 'about'})" link /> -->
                </template>
            </Toolbar>
        </nav>   
    </div>
</template>

<script setup lang="ts">
import router from '@/router'
import Toolbar from 'primevue/toolbar';
import Button from 'primevue/button';
import SplitButton from 'primevue/splitbutton';
import Sidebar from '@/components/Sidebar.vue';

const items = [
    {
        label: 'Settings',
        icon: 'pi pi-cog',
        command: () => {
            console.log('Redirecting to settings...')
        }
    },
    {
        label: 'Logout',
        icon: 'pi pi-sign-out',
        command: () => {
           console.log('Signed out.')
        }
    },
];


</script>
