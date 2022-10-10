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
        <Metrics wordCloud={place.wordCloud} sentiment={place.sentiment} visitorData={place.visitorData}/>
        <Charts busyDays={place.busyDays} busyHours={place.busyHours}/>
        <Competency competency={place.competency}/>
      </div>
    )
}

export default Layout;
