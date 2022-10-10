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

type VisitorData = {
	url: string;
}

type Props = {
	wordCloud: WordCount[] | null;
	sentiment: Sentiment | null;
	visitorData: VisitorData;
}

const Metrics: React.FC <Props> = ({wordCloud, sentiment, visitorData}) => {
  return (
		<div className='grid grid-cols-2 bg-color-red m-6 gap-6'>
			<PeopleSays wordCloud={wordCloud}/>
			<div className='grid gap-6'>
				<HeadsUp sentiment={sentiment}/>
				<Visitor visitorData={visitorData}/>
			</div>
		</div>
  );
};

export default Metrics;
