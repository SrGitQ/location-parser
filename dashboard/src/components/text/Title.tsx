import React from 'react';

type Props = {
    title: string;
}

const Title: React.FC<Props> = ({title}) => {
    return (
        <div className='text-xl text-center'>
            {title}
        </div>
    );
}

export default Title;