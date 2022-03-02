import streamlit as st
from multiapp import MultiApp
import plot, table, cplot, ctable, home

app=MultiApp()
app.add_app("HOME",home.app)
app.add_app("plot",plot.app)
app.add_app("table",table.app)
app.add_app("customplot",cplot.app)
app.add_app("customtable",ctable.app)

app.run()

