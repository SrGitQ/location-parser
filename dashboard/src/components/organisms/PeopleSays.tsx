import React from 'react'
import { MBox } from '../boxes';
import { Title } from '../text';
import ReactWordcloud from 'react-wordcloud';

type WordCount = {
	text: string;
	value: number;
};

type Props = {
    wordCloud: WordCount[] | null;
}

const options:any = {
	rotationAngles : [0, 0],
	colors: ['#b7b9bc'],
	fontFamily: 'Arial Black',
	rotations: 1,
	enableOptimizations: false,
	fontSizes: [12, 40],
	fontWeight: 'bold',
	padding: 1,
	deterministic: true,
};

const PeopleSays: React.FC <Props> = ({wordCloud}) => {
    return (
        <MBox>
            <Title title='People says'/>
            <ReactWordcloud
                options={options}
                words={wordCloud ? wordCloud : []} 
            />
        </MBox>
    );
};

export default PeopleSays;
