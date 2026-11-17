<b>Last Updated:</b> November 17, 2026

<b>1. Introduction</b><br />Bonjour, LLC ("we," "us," or "our") is committed to protecting your privacy. This Privacy Policy explains how our application, <b>Atlas for App Store Connect</b> ("the App"), handles your data.<br /><b>The core principle of Atlas is privacy-first: We do not store, access, or transmit your App Store Connect credentials to our servers.</b>

<b>2. Data Collection and Usage</b>

- <b>App Store Connect Credentials (Private Keys & Tokens):</b>
  - Your <code>.p8</code> private keys, Issuer IDs, and Key IDs are stored locally on your device or in your personal iCloud (if enabled).
  - <b>We never have access to your private keys.</b> They are processed strictly on your device to sign API requests.
- <b>Usage Data (Analytics):</b>
  - We use <b>Google Analytics for Firebase</b> to understand app interactions, screen views, sessions, and purchase events, and <b>Firebase Crashlytics</b> to diagnose crashes and non-fatal errors. These services may process an app-instance identifier, approximate location derived from masked IP addresses, device and operating-system information, crash traces, and related app state. An app-instance identifier is not your name or email address.
  - <b>Purpose:</b> This data helps us identify stability issues and improve the user experience.
  - <b>Exclusion:</b> We strictly <b>exclude</b> any sensitive information (such as API Keys, App Names, Sales Figures, or Vendor IDs) from these analytics reports.
- <b>Purchases and Subscriptions:</b>
  - Apple processes payments for Atlas Premium. We use <b>RevenueCat</b> to validate purchases, restore purchases, and manage subscription entitlements.
  - RevenueCat processes purchase and subscription records, product identifiers, transaction status, and an anonymous identifier generated for your purchases in the App. These records support app functionality, including purchase verification, restoring access, and fraud prevention, and subscription analytics.
  - Atlas does not send your App Store Connect private key, Issuer ID, Key ID, or account email address to RevenueCat as your purchase user identifier. We do not receive payment-card details from Apple.

<b>3. Data Storage and Synchronization</b>

- <b>Local Storage:</b> By default, your data is stored securely on your device using encrypted databases.
- <b>iCloud Synchronization:</b>
  - The App utilizes <b>Apple iCloud</b> services to synchronize your configuration and accounts across your devices.
  - This data is stored in your private iCloud container. Bonjour, LLC cannot access your iCloud data.

<b>4. Third-Party Services</b><br />The App uses the following third-party services, which may collect information used to identify your device:

- <b>Google Analytics for Firebase and Firebase Crashlytics:</b> [Google Privacy Policy](https://policies.google.com/privacy)
- <b>RevenueCat:</b> [RevenueCat Privacy Policy](https://www.revenuecat.com/privacy)
- <b>Apple iCloud, App Store, and App Store Connect API:</b> [Apple Privacy Policy](https://www.apple.com/legal/privacy/)

<b>5. Network Communication</b>

- <b>Direct API Connection:</b> All requests to fetch your app's data (Sales, Builds, Reviews) are sent directly from your device to Apple's servers (<code>api.appstoreconnect.apple.com</code>). We do not proxy this traffic.

<b>6. Data Retention</b><br />You have full control over your data. Deleting an account within the App or deleting the App entirely will remove the associated data from your device. If you use iCloud, data removal will propagate to your other devices.

<b>7. Contact Us</b><br />If you have any questions about this Privacy Policy, please contact us at: [support@bonjour.dev](mailto:support@bonjour.dev)
