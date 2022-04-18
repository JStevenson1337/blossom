/* global initTabs */
import React from 'react'
import Layout from '..components/Layout'
import Hero from '../components/Hero'
import StickyNav from '../components/StickyNav'
import TextRevealImageCard from '../components/TextRevealImageCard'
import TextCard from '../components/TextCard'
import 'isomorphic-fetch'
import { logPageView } from '..utils/analytics'

export default class extends React.Component {
    static async getInitialProps (){
    const apiUrl = 'https://wp.catechitics.com/wp-json/wp/';
    const params = 'pages?slug=home-black-banner&fields=ac'
    const res = await fetch(apiUrl + params)
    const data = await res.json()
    return { data }
    }

}