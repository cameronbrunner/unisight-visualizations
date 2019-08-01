#!/usr/bin/env python

import time
import json
import os
import base64

from graphqlclient import GraphQLClient


def query_allExecdHosts(client):
  result =  client.execute('''
{allHosts(arch: "lx-amd64"){Hosts {
  _id
  hostname
  cluster_name
  swapUsed
  memTotal
  arch
  swapTotal
  queueCount
  cpu
  host_count
  poll_time
  poll_epoch
  loadAvg
  numberOfProcessors
  memUsed
  resourceNumericValues
  jobCount
}}}
  ''')
  return result

def query_allJobs(client):

  result = client.execute('''
{allJobs {Jobs {
  _id
  name
  cluster_name
  command
  commandArgs
  account
  user
  queue
  queue_name
  jobid
  state
  department
  project
  parrallelEnv
  priority
  shares
  restart
  slots
  taskid
  timeStamp
  usage
  mailOpt
  wait_time_seconds
  jc_name
}}}
        ''')
  return result

def query_AllJobs_Running(client):

  result = client.execute('''
{allJobs(state: "r") {Jobs {
  _id
  name
  cluster_name
  command
  commandArgs
  account
  user
  queue
  queue_name
  jobid
  state
  department
  project
  parrallelEnv
  priority
  shares
  restart
  slots
  taskid
  timeStamp
  usage
  mailOpt
  wait_time_seconds
  jc_name
}}}
        ''')
  return result

def query_AllJobs_Queued(client):

  result = client.execute('''
{allJobs(state: "qw") {Jobs {
  _id
  name
  cluster_name
  command
  commandArgs
  account
  user
  queue
  queue_name
  jobid
  state
  department
  project
  parrallelEnv
  priority
  shares
  restart
  slots
  taskid
  timeStamp
  usage
  mailOpt
  wait_time_seconds
  jc_name
}}}
        ''')
  return result