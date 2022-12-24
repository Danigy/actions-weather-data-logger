
<div align="center">
  <!--- <img src="https://imgur.com/lCyX6TX.png"> -->
  <br>
  <br>
  <p>
    <img src="https://forthebadge.com/images/badges/made-with-python.svg">
    <img src="http://forthebadge.com/images/badges/built-with-love.svg">
  </p>
  <h1> How to Schedule a Python script with GitHub Actions to Automate timely routine tasks !</h1>
  

  <p>
    <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/Danigy/actions-weather-data-logger">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/Danigy/actions-weather-data-logger">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=shields">
    <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/Danigy/actions-weather-data-logger">
    <img alt="GitHub" src="https://img.shields.io/github/license/Danigy/actions-weather-data-logger">
    <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/Danigy/actions-weather-data-logger">
    <img alt="Maintenance" src="https://img.shields.io/maintenance/yes/2022">
    
 **Display GitHub Action Badge** [![run main.py](https://github.com/Danigy/actions-weather-data-logger/actions/workflows/actions.yml/badge.svg)](https://github.com/Danigy/actions-weather-data-logger/actions/workflows/actions.yml)
  </p>
  <p align="center">
    <a href="#usage">Usage</a> •
    <a href="#actions-yml">Actions-YML</a> •
    <a href="#environment">Environment</a> •
    <a href="#gitignore">Gitignore</a> •
     <a href="#license">License</a> •
    <a href="#main-py">main python</a> •
    <a href="#readme">Read me</a> •
     <a href="#requirments">Requirments</a> •
    <a href="#status-log">Status Log</a> 
  </p>
  <p align="center">
    <i>If this helped you  and Loved the tool? Please consider <strong>donating</strong> 💸 to help it improve!</i>
    </p>

  <p align="center">
    <a href="https://www.buymeacoffee.com/dnlmd"> <img align="center" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50" width="210" alt="Danigy" />
    </a>
    <a href="https://www.patreon.com/user?u=84162601"> <img align="center" src="https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white" height="50" width="210" alt="Danigy" />
    </a>
  </p>
</div>

<p>

<!---
<p align="center">
    <a href='https://ko-fi.com/mouadessalim' target='_blank'><img height='30' width="115" src='https://cdn.ko-fi.com/cdn/kofi3.png?v=2' alt='Buy Coffee for mouadessalim' />
    </a>
    <a href="https://www.buymeacoffee.com/mouadessalim" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="30" width="115" style="border-radius:1px" />
    </a>
  </p>
-->

This example shows how to run a Python script as cron job with GitHub Actions. It calls an API once a week (could be any schedule you want), logs the response in `status.log`, and automatically pushes the changes to this repo.

- Implement your script in `main.py`
- Inspect and configure cron job in GitHub Action `.github/workflows/actions.yml`
- It can install and use third party packages from `requirements.txt`
- Secret environment variables can be used. Set secrets in Settings/Secrets/Actions -> 'New repository secret'. 
  Use the same secret name inside `actions.yml` and `main.py`
