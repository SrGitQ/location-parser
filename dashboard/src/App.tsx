import React, {useEffect} from 'react';
import Layout from './Layout';
import Place from './utils/types';


const App: React.FC = () => {

	const [place, setPlace] = React.useState<Place | null>(null);

	useEffect(() => {
		fetch('http://localhost:5000/')
			.then(res => res.json())
			.then((place) => {
				setPlace(place);
				console.log(place);
			})
	}, []);

  	return (
		<div>
			<Layout place={place}/>
		</div>
  	);
}

export default App;
