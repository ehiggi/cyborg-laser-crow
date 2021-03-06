Vue.component('landing-page', {
    props:{
      cropData: {
          type: Object
      }
    },
    template: `
    <div class="container">
        <div class="row">
            <div>
                <div class="col-sm-12 col-md-10 col-md-offset-1">
                <label>Enter Zip Code:</label>
                <input type="text" v-model="zip">
                <select class="mdb-select md-form" v-model="crops" multiple>
                    <option>Corn</option>
                    <option>Wheat</option>
                    <option>Barley</option>
                    <option>Soybean</option>
                    <option>Cotton</option>
                </select>
                <button @click="lookup">Submit</button>
                </div>
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
Vue.component('weather-app',{
    props:{
        data: {
            type: Array
        }
    },
   template: `
   <div>
   <div v-for="day in data" class="weather-box">
   <div class="column">
       <h3>{{day.date}}</h3>
       <h4>Low: {{day.low}} &deg;C</h4>
       <h4>High: {{day.high}} &deg;C</h4>
   </div>
   <div class="column">
    <h4 style="text-align:right;">{{day.weather}}</h4>
   </div>
</div>
</div>
   `
});
Vue.component('price-table', {
    props: {
        crops: {
            type: Array
        },
        priceData: {
            type: Object,
        }
    },
    template: `
    <div class="container" >
        <table v-for="crop in crops"> {{crops[crop]}}
            <tr>
                <th v-for="key in priceHeaders">{{key}}</th>
            </tr>
            <tr v-for">
                <td v-for="key in priceHeaders">{{cropPrices[crops[crop]][key][list[entry]]}}</td>
            </tr>
        </table>
    </div>
    `,

    methods:{
        lookup:function () {
            this.$emit('complete-search',this.zip, this.crops)
        }
    },
    computed: {
        cropPrices() {
            var crop_dict = {};
            for (key in this.priceData) {
                if (this.priceData.key) {
                    crop_dict[key]= this.priceData.key
                }
            }
            return crop_dict
        },
        cropTypes(){
            var c_list = [];
            for (var key in this.cropPrices) {
                c_list.push(key);
            }
            return c_list
        },
        priceHeaders(){
            var c_list = [];
            for (var key in this.cropPrices[this.cropTypes[0]]) {
                c_list.push(key);
            }
            return c_list
        },

    },
    data() {
            return {
                list: ['1','2','3','4','5','6','7','8','9','10']
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
    },
    computed: {
        weatherData() {
            return this.fullData.weather
        }
    }

});

function fetch_all(zip,crops) {
    var cropStr = '';
    for (var crop in crops) {
        if (cropStr == '') {
            cropStr = crops[crop];
        }
        else{
            cropStr += ',' + crops[crop];
        }
    }

    fetch(`http://${window.location.hostname}:5000/data?zip=${zip}&crops=${cropStr}`, {}) .then(response => response.json()) .then(success => (app.$data.fullData = success)) .catch(error => console.log(error))
}
