import React from 'react';
import { PeopleSays, HeadsUp, Visitor } from './organisms';

type WordCount = {
	text: string;
	value: number;
};

type Sentiment = {
	positive: number;
	neutral: number;
	negative: number;
}


type Props = {
	wordCloud: WordCount[] | null;
	sentiment: Sentiment | null;
	website: string;
    id:string;
}

const Metrics: React.FC <Props> = ({wordCloud, sentiment, website, id}) => {
  return (
		<div className='grid grid-cols-2 bg-color-red m-6 gap-6'>
			<PeopleSays wordCloud={wordCloud}/>
			<div className='grid gap-6'>
				<HeadsUp sentiment={sentiment}/>
				<Visitor website={website} id={id}/>
			</div>
		</div>
  );
};

export default Metrics;
