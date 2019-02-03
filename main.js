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
        <table>
            <tr>
                <th v-for="key in priceHeaders">{{key}}</th>
            </tr>
            <tr v-for="entry in list">
                <td v-for="key in priceHeaders">{{priceData[key][list[entry]]}}</td>
            </tr>
        </table>
    </div>
    `,
    data() {
        return {
            priceData: {
                "Year":{"1":2017,"2":2016,"3":2015,"4":2014,"5":2013,"6":2012,"7":2011,"8":2010,"9":2009,"10":2008},
                "PRICE":{"1":"9.39","2":"9.39","3":"9.49","4":"12.5","5":"14.1","6":"14","7":"12.5","8":"9.97","9":"10.1","10":"11.3"},
                "YIELD":{"1":49.3,"2":52.0,"3":48.0,"4":47.5,"5":44.0,"6":40.0,"7":42.0,"8":43.5,"9":44.0,"10":39.7}},
            list: ['1','2','3','4','5','6','7','8','9','10']
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

