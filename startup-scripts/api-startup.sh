#!/bin/bash
uwsgi --emperor /etc/risk_models_api/uwsgi/*.ini &
nginx;