# -*- coding: utf-8 -*- #
# Copyright 2019 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Common utility functions for Cloud Filestore update snapshot commands."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from apitools.base.py import encoding
from googlecloudsdk.api_lib.filestore import filestore_client
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.util.args import labels_util
from googlecloudsdk.core import properties
from googlecloudsdk.core import resources


def AdditionalSnapshotUpdateArguments():
  return SnapshotUpdateLabelsFlags()


def SnapshotUpdateLabelsFlags():
  remove_group = base.ArgumentGroup(mutex=True)
  remove_group.AddArgument(labels_util.GetClearLabelsFlag())
  remove_group.AddArgument(labels_util.GetRemoveLabelsFlag(''))
  return [labels_util.GetUpdateLabelsFlag(''), remove_group]


def UpdateLabels(ref, args, req):
  """Update snapshot labels."""
  ref = GetResourceRef(args)
  labels_diff = labels_util.Diff.FromUpdateArgs(args)
  if labels_diff.MayHaveUpdates():
    req = AddFieldToUpdateMask('labels', req)
    messages = GetMessagesForResource(ref)
    new_labels = labels_diff.Apply(messages.Snapshot.LabelsValue,
                                   req.snapshot.labels).GetOrNone()
    if new_labels:
      req.snapshot.labels = new_labels
  return req


def AddDescription(unused_instance_ref, args, patch_request):
  del unused_instance_ref
  if args.IsSpecified('description'):
    patch_request.snapshot.description = args.description
    patch_request = AddFieldToUpdateMask('description', patch_request)
  return patch_request


def AddFieldToUpdateMask(field, patch_request):
  update_mask = patch_request.updateMask
  if update_mask:
    if update_mask.count(field) == 0:
      patch_request.updateMask = update_mask + ',' + field
  else:
    patch_request.updateMask = field
  return patch_request


def GetMessagesForResource(resource_ref):
  api_version = resource_ref.GetCollectionInfo().api_version
  messages = filestore_client.GetMessages(api_version)
  return messages


def GetResourceRef(args):
  project = properties.VALUES.core.project.Get(required=True)
  location = args.region or args.zone
  ref = resources.REGISTRY.Create(
      'file.projects.locations.snapshots', projectsId=project,
      locationsId=location, snapshotsId=args.snapshot)
  return ref


def GetExistingSnapshot(resource_ref, args, patch_request):
  """Fetch existing Filestore instance to update and add it to Patch request."""
  resource_ref = GetResourceRef(args)
  api_version = resource_ref.GetCollectionInfo().api_version
  client = filestore_client.FilestoreClient(api_version)
  orig_snapshot = client.GetSnapshot(resource_ref)
  patch_request.snapshot = orig_snapshot
  return patch_request


def FormatSnapshotUpdateResponse(response, args):
  """Python hook to generate the snapshot update response."""
  del response
  # Return snapshot describe output.
  resource_ref = GetResourceRef(args)
  api_version = resource_ref.GetCollectionInfo().api_version
  client = filestore_client.FilestoreClient(api_version)
  return encoding.MessageToDict(client.GetSnapshot(resource_ref))
