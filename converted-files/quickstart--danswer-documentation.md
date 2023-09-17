[Danswer Documentation home page![light logo](https://mintlify.s3-us-
west-1.amazonaws.com/danswer/logo/light.png)![dark
logo](https://mintlify.s3-us-west-1.amazonaws.com/danswer/logo/dark.png)](/)

Search...

  * [danswer-ai/danswer](https://github.com/danswer-ai/danswer)
  * [danswer-ai/danswer](https://github.com/danswer-ai/danswer)

Switch theme

Search

Navigation

Welcome to Danswer

Quickstart

  * [Documentation](/)
  * [Slack](https://join.slack.com/t/danswer/shared_invite/zt-1u3h3ke3b-VGh1idW19R8oiNRiKBYv2w)
  * [Discord](https://discord.gg/TDJ59cGV2X)

##### Welcome to Danswer

  * [Introduction](/introduction)
  * [Quickstart](/quickstart)
  * [Google OAuth Setup](/google_oauth_setup)
  * [Enterprise Setup](/enterprise_setup)
  * [Slack Bot Setup](/slack_bot_setup)
  * Gen AI Configs

  * [System Overview](/system_overview)
  * [Contact Us](/contact_us)

##### Connectors

  * [Connector Overview](/connectors/overview)
  * [Web Connector](/connectors/web)
  * [File Connector](/connectors/file)
  * [Slack Connector](/connectors/slack)
  * [GitHub Connector](/connectors/github)
  * [Confluence Connector](/connectors/confluence)
  * [Jira Connector](/connectors/jira)
  * Google Drive Connector

  * [Notion Connector](/connectors/notion)
  * [BookStack Connector](/connectors/bookstack)
  * [Guru Connector](/connectors/guru)
  * [Productboard Connector](/connectors/productboard)
  * [Zulip Connector](/connectors/zulip)

Welcome to Danswer

# Quickstart

How to deploy Danswer on your local machine

##

​

Requirements

  * git
  * docker with compose (docker version >= 1.13.0)

##

​

Setup

**This quickstart guide covers setting up Danswer for local execution**

  1. Clone the [Danswer](https://github.com/danswer-ai/danswer) repo: `git clone https://github.com/danswer-ai/danswer.git`
  2. Navigate to **danswer/deployment/docker_compose**
  3. Bring up your docker engine and run:
    * To pull images from DockerHub and run Danswer:
      * `docker compose -f docker-compose.dev.yml -p danswer-stack up -d --pull always --force-recreate`
    * Alternatively, to build the containers from source and start Danswer, run:
      * `docker compose -f docker-compose.dev.yml -p danswer-stack up -d --build --force-recreate`
    * These commands are also used to redeploy if any **.env** variables are updated
    * This may take 15+ minutes depending on your internet speed.
  4. Danswer will now be running on <http://localhost:3000>.

##

​

OpenAI API Key

**Note:** On the initial visit, Danswer will prompt for an OpenAI API key.
Without this Danswer will be able to provide search functionalities but not
direct Question Answering.

You can get an OpenAI API key at: <https://platform.openai.com/account/api-
keys>

##

​

Indexing Documents

**This quickstart guide will index a publicly accessible website as this
requires no additional authorization setup**

  1. Navigate to the top right of Danswer’s home screen and select **Admin Panel**

![Connectors](https://mintlify.s3-us-
west-1.amazonaws.com/danswer/images/quickstart/DanswerConnectors.png)

  2. In the Web Connector dashboard, pick any base URL to index.
    * This will index all pages under that base URL that is reachable from hyperlinks.
    * You can check the indexing status page to monitor the progress.

![WebConnector](https://mintlify.s3-us-
west-1.amazonaws.com/danswer/images/quickstart/DanswerWebConnector.png)

  3. After the pages are indexed, you can now navigate back to the homepage and start asking questions and getting answers! 🥳

![SampleQA](https://mintlify.s3-us-
west-1.amazonaws.com/danswer/images/quickstart/DanswerSampleQA.png)

##

​

Shutting Down

  1. `docker compose -f docker-compose.dev.yml -p danswer-stack down`
    * add `-v` at the end to delete the volumes (containing users and indexed documents)

[Introduction](/introduction)[Google OAuth Setup](/google_oauth_setup)

[github](https://github.com/danswer-
ai/danswer)[twitter](https://twitter.com/DanswerAI)[linkedin](https://linkedin.com/company/danswerai)

[Powered by
Mintlify](https://mintlify.com?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.danswer.dev)

  * Requirements
  * Setup
  * OpenAI API Key
  * Indexing Documents
  * Shutting Down

