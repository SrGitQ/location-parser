import React from 'react';
import { BasicInformation, Metrics, Charts, Competency, CompetencyLayer } from './components';
import Place from './utils/types';

type Props = {
  place: Place | null;
};


const Layout: React.FC <Props> = ({place}) => {
    return place ? (
        
      <div className="grid-rows-4">
        <BasicInformation place={place}/>
        <Metrics wordCloud={place.wordCloud} sentiment={place.sentiment} website={place.website} id={place.place_id}/>
        <Charts busyDays={place.busyDays} busyHours={place.busyHours}/>
        {place.competency?.length > 0 ? <CompetencyLayer place={place}/> : null}
      </div>
    ) : (<></>)
}

export default Layout;
