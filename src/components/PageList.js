import PageItem from "./PageItem"
import classes from "./PageList.module.css"

function PageList(props) {
  return (
    <div>
      {Object.keys(props.pages).map((page, i) => { //Loop into each page
        //console.log("PageListPage")
        //console.log(page)
        return (
          <div className={classes.box} key={props.sections[i].id} id={props.sections[i].id}>
            <h1 className={classes.textCenter}>
              {page //Display page name
              }
            </h1>
            <PageItem items={props.pages[page]}/>
        </div>
        ) 
      })}
    </div>
  )
}
export default PageList