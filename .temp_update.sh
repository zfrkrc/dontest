#!/bin/bash
# Script to update all Dockerfile COPY paths for new build context

# Simple services (arjun, dirsearch, dnsrecon, sslyze, wafw00f)
for service in arjun dirsearch dnsrecon sslyze wafw00f whatweb; do
  echo "Updating $service..."
done
