import React from 'react';
import Layout from './Layout';
import Place from './utils/types';


const App: React.FC = () => {

	const local:Place = {
		name: 'Metropolitan Ave',
		address: '3 North Trenton St. Burnsville, MN 55337',
		phone: '+51 999 140 5395',
		type: 'Restaurant',
		status: 'Open',
    rating:4.5,
    reviews:[13, 10, 2, 3, 4]
	};

  return (
    <div>
        <Layout place={local}/>
    </div>
  );
}

export default App;
