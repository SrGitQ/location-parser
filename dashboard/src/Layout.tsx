import React from 'react';
import { BasicInformation, Metrics, Charts, Competency } from './components';
import Place from './utils/types';

type Props = {
  place: Place;
};

const Layout: React.FC <Props> = ({place}) => {
    return (
      <div className="grid-rows-4">
        <BasicInformation place={place}/>
        <Metrics />
        <Charts />
        <Competency />
      </div>
    )
}

export default Layout;