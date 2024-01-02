/*****************************
 * environment.js
 * path: '/environment.js' (root of your project)
 ******************************/

import * as Updates from 'expo-updates'

const ENV = {
  development: {
    GRAPHQL_URL: 'https://prodenategamultivendorapi.herokuapp.com/graphql', // [Enter  your server url:Enter your port number followed by any port number followed by graphql][example: http://192.168.100.117:8001/graphql]
    WS_GRAPHQL_URL: 'wss://prodenategamultivendorapi.herokuapp.com/graphql', // [Append with ws:// if in development otherwise wss:// followed by your ip and port number followed by graphql][example: ws://192.168.100.97:8001/graphql]
    SENTRY_DSN: 'https://e963731ba0f84e5d823a2bbe2968ea4d@o1103026.ingest.sentry.io/6135261', // [Add your own Sentry DSN link][example: https://e963731ba0f84e5d823a2bbe2968ea4d@o1103026.ingest.sentry.io/5135261]
    GOOGLE_MAPS_KEY: 'AIzaSyCzNP5qQql2a5y8lOoO-1yj1lj_tzjVImA' // [Add your Google map key see documentation for more information][example: BIzaSyCzNP5qQql2a5y8lOoO - 1yj1lj_tzjVImA]
  },
  staging: {
    GRAPHQL_URL: 'https://stagingenategamultivendorapi.herokuapp.com/graphql',
    WS_GRAPHQL_URL: 'wss://stagingenategamultivendorapi.herokuapp.com/graphql',
    SENTRY_DSN: '', // [Add your own Sentry DSN link][example: https://e963731ba0f84e5d823a2bbe2968ea4d@o1103026.ingest.sentry.io/5135261]
    GOOGLE_MAPS_KEY: '' // [Add your Google map key see documentation for more information][example: BIzaSyCzNP5qQql2a5y8lOoO - 1yj1lj_tzjVImA]
  },
  production: {
    GRAPHQL_URL: 'https://prodenategamultivendorapi.herokuapp.com/graphql',
    WS_GRAPHQL_URL: 'wss://prodenategamultivendorapi.herokuapp.com/graphql',
    SENTRY_DSN: 'https://e963731ba0f84e5d823a2bbe2968ea4d@o1103026.ingest.sentry.io/6135261', // [Add your own Sentry DSN link][example: https://e963731ba0f84e5d823a2bbe2968ea4d@o1103026.ingest.sentry.io/5135261]
    GOOGLE_MAPS_KEY: 'AIzaSyCzNP5qQql2a5y8lOoO-1yj1lj_tzjVImA' // [Add your Google map key see documentation for more information][example: BIzaSyCzNP5qQql2a5y8lOoO - 1yj1lj_tzjVImA]
  }
}

const getEnvVars = (env = Updates.releaseChannel) => {
  // What is __DEV__ ?
  // This variable is set to true when react-native is running in Dev mode.
  // __DEV__ is true when run locally, but false when published.
  // eslint-disable-next-line no-undef
  if (env === 'production') {
    return ENV.production
  } else if (env === 'staging') {
    return ENV.staging
  } else {
    return ENV.development
  }
}

export default getEnvVars
