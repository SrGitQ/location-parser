import React from 'react';
import Layout from './Layout';
import Place from './utils/types';


const App: React.FC = () => {

	const local:Place = {
    img:{src:'https://www.collinsdictionary.com/images/full/restaurant_135621509_1000.jpg?version=4.0.279'},
    name:'Metropolitan Ave',
    type:'Restaurant',
    phone:'+51 999 140 5395',
    status:'Closed',
    rating:4.5,
    location:{lat:20.9863018, lng:-89.733405},
    address:'3 North Trenton St. Burnsville, MN 55337',
    visitorData:{url:'www.google.com'},
    competency:null,
    busyDays: {days:[{day: 'M',people: 30,},{day: 'T',people: 20,},{day: 'W',people: 30,},{day: 'T',people: 10,},{day: 'F',people: 20,},{day: 'S',people: 30,},{day: 'S',people: 40}]},
    sentiment:{positive: 40, neutral: 20, negative: 30},
    wordCloud:[{text: 'told', value: 1},{text: 'mistake', value: 11},{text: 'thought', value: 16},{text: 'bad', value: 17}],
    reviews:[13, 10, 2, 3, 4],
    busyHours: {hours:[{hour: '1',people: 10,},{hour: '2',people: 20,},{hour: '3',people: 30,},{hour: '4',people: 30,},{hour: '5',people: 50,},{hour: '6',people: 60,},{hour: '7',people: 20,},{hour: '8',people: 10,},{hour: '9',people: 70,},{hour: '10',people: 100,},{hour: '11',people: 10,},{hour: '12',people: 20,},{hour: '13',people: 30,},{hour: '14',people: 50,},{hour: '15',people: 50,},{hour: '16',people: 60,},{hour: '17',people: 70,},{hour: '18',people: 20,},{hour: '19',people: 58,},{hour: '20',people: 40,},{hour: '21',people: 10,},{hour: '22',people: 20,},{hour: '23',people: 30,},{hour: '24',people: 40,}]},
  };

  local.competency = [local, local, local, local, local]

  return (
    <div>
        <Layout place={local}/>
    </div>
  );
}

export default App;
