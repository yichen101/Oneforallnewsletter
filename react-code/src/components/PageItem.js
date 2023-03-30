import classes from './PageItem.module.css'

function PageItem(props) {
    return (
        <div>
            {Object.keys(props.items).map((item, index) => { //Loop into each item
                //console.log("ITEMTITLE")
                //console.log(props.items[item].title)
                return (
                    <div>
                        <li>
                            <div className={classes.card}>
                                <a href = {"//"+props.items[item].link} target="_blank" className={classes.title}>
                                    {props.items[item].title}
                                </a>
                            </div>
                        </li>
                    </div>
                )
            })}
        </div>
    )
}

export default PageItem