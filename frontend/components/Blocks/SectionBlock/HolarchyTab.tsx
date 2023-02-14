export default function HolarchyTab() {
  return (
    <div className="w-screen h-screen bg-white">
      <div className="bg-white fixed top-[4.5rem] md:top-24 inset-x-0 mx-auto h-[calc(100%-4.5rem)] md:h-[calc(100%-9.5rem)] w-screen z-10 mt-14 grid grid-rows-9 grid-cols-1 md:grid-cols-3 md:grid-rows-3 ">
        {/*National level*/}
        {/*National interactive input */}
        <div className="p-4 bg-holon-blue-100 overflow-auto row-start-1 row-span-1 col-start-1 col-span-1 md:col-start-1 md:col-span-1 md:row-start-1 md:row-span-1 border-b-2 border-dashed border-holon-blue-900 ">
          <p>Nationaal interactive input</p>
        </div>

        {/*image */}
        <div className="row-start-4 bg-holon-blue-100 row-span-1 col-start-1 col-span-1 md:col-start-2 md:col-span-1 md:row-start-1 md:row-span-1">
          <div className="row-start-4 row-span-3 md:col-start-2 md:col-span-1 md:row-start-1 md:row-span-3">
            {/* eslint-disable @next/next/no-img-element */}
            {/*<img src={} alt={} width="900" height="1600" />*/}
          </div>

          <p>Hier komt een image</p>
        </div>

        {/*National KPIs */}
        <div className=" p-4 bg-holon-blue-100 row-start-7 row-span-1 col-start-1 col-span-1 md:col-start-3 md:col-span-1 md:row-start-1 md:row-span-1 border-b-2 border-dashed border-holon-blue-900">
          <p>
            Nationale KPI<span>&#39;</span>s
          </p>
        </div>

        {/*Middle level*/}
        {/*Middle interactive input */}
        <div className="p-4 bg-holon-blue-200 overflow-auto row-start-2 row-span-1 col-start-1 col-span-1 md:col-start-1 md:col-span-1 md:row-start-2 md:row-span-1 border-b-2 border-dashed border-holon-blue-900">
          <p>Midden interactive input </p>
        </div>

        {/*image */}
        <div className="bg-holon-blue-200 row-start-5 row-span-1 col-start-1 col-span-1 md:col-start-2 md:col-span-1 md:row-start-2 md:row-span-1">
          <p></p>
        </div>

        {/*Middle KPIs */}
        <div className=" p-4 bg-holon-blue-200 row-start-8 row-span-1 col-start-1 col-span-1 md:col-start-3 md:col-span-1 md:row-start-2 md:row-span-1 border-b-2 border-dashed border-holon-blue-900">
          <p>
            Tussen KPI<span>&#39;</span>s
          </p>
        </div>

        {/*Local level*/}
        {/*Local interactive input */}
        <div className=" p-4 bg-holon-blue-300 overflow-auto row-start-3 row-span-1 col-start-1 col-span-1 md:col-start-1 md:col-span-1 md:row-start-3 md:row-span-1 border-b-2 border-dashed border-holon-blue-900">
          <p>Lokaal interactive input</p>
        </div>

        {/*image */}
        <div className="bg-holon-blue-300  row-start-6 row-span-1 col-start-1 col-span-1 md:col-start-2 md:col-span-1 md:row-start-3 md:row-span-1">
          <p></p>
        </div>

        {/*Local KPIs */}
        <div className=" p-4 bg-holon-blue-300  row-start-9 row-span-1 col-start-1 col-span-1 md:col-start-3 md:col-span-1 md:row-start-3 md:row-span-1 border-b-2 border-dashed border-holon-blue-900">
          <p>
            Lokale KPI<span>&#39;</span>s
          </p>
        </div>
      </div>
    </div>
  );
}
