<template>
      <div class="card">
        <DataTable v-model:filters="filters" :value="customers" paginator showGridlines removableSort :rows="10" dataKey="id"
                filterDisplay="menu" :loading="loading" :globalFilterFields="['name', 'country.name', 'representative.name', 'balance', 'status']">
            <template #header>
                <div class="flex justify-between">
                    <Button type="button" class="mr-2" icon="pi pi-filter-slash" label="Clear" outlined @click="clearFilter()" />
                    <span class="relative">
                        <i class="pi pi-search absolute top-2/4 -mt-2 left-3 text-surface-400 dark:text-surface-600" />
                        <InputText v-model="filters['global'].value" placeholder="Global Search"  class="pl-10 font-normal"/>
                    </span>
                </div>
            </template>
            <template #empty> No data found. </template>
            <template #loading> Loading data. Please wait. </template>
            <Column field="name" header="Name" sortable style="min-width: 12rem">
                <template #body="{ data }">
                    {{ data.name }}
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" class="p-column-filter" placeholder="Search by name" />
                </template>
            </Column>
            <Column header="Country" field="country" sortable style="min-width: 12rem">
                <template #body="{ data }">
                    <div class="flex items-center gap-2">
                        <span>{{ data.country }}</span>
                    </div>
                </template>
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" class="p-column-filter" placeholder="Search by country" />
                </template>
                <!-- <template #filterclear="{ filterCallback }">
                    <Button type="button" icon="pi pi-times" @click="filterCallback()" severity="secondary"></Button>
                </template>
                <template #filterapply="{ filterCallback }">
                    <Button type="button" icon="pi pi-check" @click="filterCallback()" severity="success"></Button>
                </template> -->
                <!-- <template #filterfooter>
                    <div class="px-3 pt-0 pb-3 text-center">Customized Buttons</div>
                </template> -->
            </Column>
            <Column header="Date" field="date" dataType="date" sortable style="min-width: 10rem">
                <template #body="{ data }">
                    {{ formatDate(data.date) }}
                </template>
                <template #filter="{ filterModel }">
                    <Calendar v-model="filterModel.value" dateFormat="mm/dd/yy" placeholder="mm/dd/yyyy" mask="99/99/9999" />
                </template>
            </Column>
            <!-- <Column header="Balance" filterField="balance" dataType="numeric" style="min-width: 10rem">
                <template #body="{ data }">
                    {{ formatCurrency(data.balance) }}
                </template>
                <template #filter="{ filterModel }">
                    <InputNumber v-model="filterModel.value" mode="currency" currency="USD" locale="en-US" />
                </template>
            </Column> -->
            <!-- <Column header="Status" field="status" :filterMenuStyle="{ width: '14rem' }" style="min-width: 12rem">
                <template #body="{ data }">
                    <Tag :value="data.status" :severity="getSeverity(data.status)" />
                </template>
                <template #filter="{ filterModel }">
                    <Dropdown v-model="filterModel.value" :options="statuses" placeholder="Select One" class="p-column-filter" showClear>
                        <template #option="slotProps">
                            <Tag :value="slotProps.option" :severity="getSeverity(slotProps.option)" />
                        </template>
                    </Dropdown>
                </template>
            </Column> -->
        </DataTable>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import dayjs from 'dayjs';

import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import Calendar from 'primevue/calendar';
import Tag from 'primevue/tag';


import { FilterMatchMode, FilterOperator } from 'primevue/api';

const customers = ref();
const filters = ref();
const loading = ref(true);

onMounted(() => {
    setTimeout(() => {
        customers.value = [
            {
                'name': 'Renz',
                'country': 'US',
                'date': new Date(dayjs().add(15, 'day').format('YYYY-MM-DD')),
            },
            {
                'name': 'Casey',
                'country': 'Russia',
                'date': new Date(dayjs().format('YYYY-MM-DD')),
            },
            {
                'name': 'Damis',
                'country': 'China',
                'date': new Date(dayjs().add(7, 'day').format('YYYY-MM-DD')),
            }
        ];
        loading.value = false;
    }, 1000)
    
    
});


const initFilters = () => {
    filters.value = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS },
        name: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
        country: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
        date: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.DATE_IS }] },
        balance: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] },
        status: { operator: FilterOperator.OR, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] },
    };
};

initFilters();

const formatDate = (value) => {
    return value.toLocaleDateString('en-US', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric'
    });
};
const formatCurrency = (value) => {
    return value.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
};
const clearFilter = () => {
    initFilters();
};
const getCustomers = (data) => {
    return [...(data || [])].map((d) => {
        d.date = new Date(d.date);

        return d;
    });
};
const getSeverity = (status) => {
    switch (status) {
        case 'unqualified':
            return 'danger';

        case 'qualified':
            return 'success';

        case 'new':
            return 'info';

        case 'negotiation':
            return 'warning';

        case 'renewal':
            return null;
    }
};
</script>