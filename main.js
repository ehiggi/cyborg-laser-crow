Vue.component('landing-page', {
    template: `
    <div class="container">
        <div class="row">
                <div class="col-sm-3 col-md-10 col-md-offset-1">
                <label>Enter Zip Code:</label>
                <input type="text" v-model="zip">
                <select name="crops" v-model="crops" data-selectr-opts='{ "title": "Desired crops?", "placeholder": "Search crops" }'  multiple>
                    <option data-selectr-color="rgb(186, 169, 20)">Barley</option>
                    <option data-selectr-color="rgb(244, 224, 45)">Corn</option>
                    <option data-selectr-color="rgb(0, 0, 0)">Cotton</option>
                    <option data-selectr-color="rgb(186, 169, 20)">Wheat</option>
                </select>
                <button @click="lookup">FARM SEARCH</button>
                </div>
        </div>
    </div>
    `,
    data() {
        return {
            zip: 0,
            crops: []
        }
    },
    methods:{
        lookup:function () {
            this.$emit('complete-search',this.zip, this.crops)
        }
    }
});
Vue.component('weather', {
    props: {
        weatherData: {
            type: Object,
            required: true
        }
    },
    template: `
    <div class="container" >
        <div class="col-xl">
            <div>
                <label>Enter Zip Code:</label>
                <input type="text" v-model="zip">
                <select class="mdb-select md-form" v-model="crops" multiple>
                    <option>Corn</option>
                    <option>Wheat</option>
                    <option>Barley</option>
                    <option>Soybeans</option>
                    <option>Cotton</option>
                    <option>Cowmoji</option>
                </select>
                <button @click="lookup">FARM SEARCH</button>
            </div>
        </div>
    </div>
    `,
    data() {
        return {
            zip: this.zipProp,
            crops: this.cropsProp
        }
    },
    methods:{
        lookup:function () {
            this.$emit('complete-search',this.zip, this.crops)
        }
    }
});
var app= new Vue({
    el: '#app',
    data:{
        fullData: [],
        zipCode: 0,
        crops: [],
        hasSearched: false
    },
    methods:{
        search: function(zip,crops){
            this.hasSearched = true;
            this.zipCode = zip;
            this.crops = crops;
            fetch_all(zip,crops);
        }
    }

});

function fetch_all(zip,crops) {
    var cropStr = '';
    for (var crop in crops) {
        if (cropStr == '') {
            cropStr = crop;
        }
        else{
            cropStr += ',' + crop;
        }
    }

    fetch(`http://${window.location.hostname}:5000/data?zip=${zip}&crops=${cropstr}`, {}) .then(response => response.json()) .then(success => (app.$data.fullData = success)) .catch(error => console.log(error))
}

