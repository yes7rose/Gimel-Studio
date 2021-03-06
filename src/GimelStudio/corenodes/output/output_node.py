# THIS FILE IS A PART OF GIMEL STUDIO AND IS LICENSED UNDER THE SAME TERMS:
# ----------------------------------------------------------------------------
# Gimel Studio Copyright 2019-2020 by Noah Rahm and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------

from GimelStudio import api


class OutputNode(api.NodeBase):
    def __init__(self, _id):
        api.NodeBase.__init__(self, _id)
        self.Model._isOutput = True
        self.Model.UpdateSockets()

        self.NodeSetThumb(self.Model.GetThumbImage())

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "Output",
            "author": "Correct Syntax",
            "version": (0, 1, 3),
            "supported_app_version": (0, 5, 0),
            "category": "OUTPUT",
            "description": """The most important node of them all. :)
        This is registered here for the UI -the evaluation is handled elsewhere.
        This node should not be accessed by outside users.
        """
        }
        return meta_info

    def NodeInitParams(self):
        p = api.RenderImageParam('Image')
        self.NodeAddParam(p)

    def NodeEvaluation(self, eval_info):
        pass


api.RegisterNode(OutputNode, "corenode_outputcomposite")
