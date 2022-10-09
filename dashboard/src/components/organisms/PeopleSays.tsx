import React from 'react'
import { MBox } from '../boxes';
import { Title } from '../text';
import ReactWordcloud from 'react-wordcloud';

type Props = {
    words: any;
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

const PeopleSays: React.FC <Props> = ({words}) => {
    return (
        <MBox>
            <Title title='People says'/>
            <ReactWordcloud
                options={options}
                words={words} 
            />
        </MBox>
    );
};

export default PeopleSays;